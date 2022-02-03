# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.util.RequestExceptions import ValueRequiredException
from app.stock.service.ProductService import ProductService
from app.stock.service.ProductValidator import ProductValidator
from app.user.service.UserLogsService import UserLogsService


class ProductController(Resource):

  def __init__(self):
    self.productService = ProductService()
    self.productValidator = ProductValidator()
    self.userLogsService = UserLogsService()

  def get(self):  
    product_id = request.args.get('product_id', None)
    app.logger.info(f"ProductController#get START - Request received - userAgent={request.user_agent.string}")

    try: 
        product = self.productValidator.validate_product_exist(product_id)

        self.userLogsService.create_log(product_id)

        app.logger.info(f"ProductController#get SUCCESS - Product retrieved - productID={product.id}")

        return jsonify(data=product.serialize())
    except ValueRequiredException as vex:
        return abort(400, message=str(vex))
    except AssertionError as assertionError:
        error_message = str(assertionError)
        app.logger.error(f'ProductController#get FAILURE - Can not get product - reason={error_message}')
        return abort(400, message=error_message)


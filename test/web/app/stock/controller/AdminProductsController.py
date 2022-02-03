# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.util.RequestExceptions import ValueRequiredException
from app.stock.service.ProductService import ProductService
from app.stock.service.ProductValidator import ProductValidator


class AdminProductsController(Resource):

    method_decorators = {
        # 'get': [SecuredSystemMiddleware.validate_token_admin]
    }

    def __init__(self):
        self.productService = ProductService()
        self.productValidator = ProductValidator()

    def get(self):
        admin_user_id = request.args.get('admin_user_id', None)

        app.logger.info(f"AdminProductsController#get START - Request received - userAgent={request.user_agent.string}")

        try: 
            # self.adminAuthValidator.validate_admin_request(request.args)

            products = self.productService.get_all()

            app.logger.info(f"AdminProductsController#get SUCCESS - Products retrieved - countCategories={len(products)} adminUserId={admin_user_id}")

            return jsonify(data=products)
        except ValueRequiredException as vex:
            return abort(400, message=str(vex))
        except AssertionError as assertionError:
            error_message = str(assertionError)
            app.logger.error(f'AdminProductsController#get FAILURE - Can not get products - reason={error_message}')
            return abort(400, message=error_message)


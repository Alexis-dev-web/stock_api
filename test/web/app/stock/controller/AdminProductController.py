# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.util.error_mesages import messages
from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from app.util.RequestExceptions import ValueRequiredException
from app.stock.service.ProductService import ProductService
from app.stock.service.ProductValidator import ProductValidator


class AdminProductController(Resource):

    method_decorators = {
        'get': [SecuredSystemMiddleware.validate_token_admin]
    }

    def __init__(self):
      self.productService = ProductService()
      self.productValidator = ProductValidator()

    def get(self):
      admin_user_id = request.args.get('admin_user_id', None)
      product_id = request.args.get('product_id', None)

      app.logger.info(f"AdminProductController#get START - Request received - userAgent={request.user_agent.string}")

      try: 
          product = self.productValidator.validate_product_exist(product_id)

          app.logger.info(f"AdminProductController#get SUCCESS - Product retrieved - productId={product.id} adminUserId={admin_user_id}")

          return jsonify(data=product.serialize())
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
          error_message = str(assertionError)
          app.logger.error(f'AdminProductController#get FAILURE - Can not get categories - reason={error_message}')
          return abort(400, message=error_message)

    def post(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminProductController#post START - Request received - userAgent={request.user_agent.string}")

      try: 
          self.productValidator.validate_create_product(request.json)

          product = self.productService.create_product(request.json)

          app.logger.info(f"AdminProductController#post SUCCESS - Product retrieved - productId={product.id}")

          return jsonify(data=product.serialize())
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
          error_message = str(assertionError)
          app.logger.error(f'AdminProductController#post FAILURE - Can not create product - reason={error_message}')
          return abort(400, message=error_message)

    def patch(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminProductController#patch START - Request received - userAgent={request.user_agent.string}")

      try: 
          product = self.productValidator.validate_update_product(request.json)

          product = self.productService.update(request.json, product)

          app.logger.info(f"AdminProductController#patch SUCCESS - Product retrieved - productId={product.id}")

          return jsonify(data=product.serialize())
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
          error_message = str(assertionError)
          app.logger.error(f'AdminProductController#patch FAILURE - Can not create product - reason={error_message}')
          return abort(400, message=error_message)

    def delete(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminProductController#delete START - Request received - userAgent={request.user_agent.string}")

      try: 
          product = self.productValidator.validate_product_exist(request.json.get('product_id', None))

          product = self.productService.delete_product(product)

          app.logger.info(f"AdminProductController#delete SUCCESS - Product retrieved - productId={product.id}")

          return '', 204
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
          error_message = str(assertionError)
          app.logger.error(f'AdminProductController#delete FAILURE - Can not create product - reason={error_message}')
          return abort(400, message=error_message)


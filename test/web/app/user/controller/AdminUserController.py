# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.util.error_mesages import messages
from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from app.util.RequestExceptions import ValueRequiredException
from app.user.service.UserService import UserService
from app.user.service.UserValidator import UserValidator


class AdminUserController(Resource):

    method_decorators = {
        # 'get': [SecuredSystemMiddleware.validate_token_admin]
    }

    def __init__(self):
      self.userService = UserService()
      self.userValidator = UserValidator()

    def get(self):
      admin_user_id = request.args.get('admin_user_id', None)
      product_id = request.args.get('product_id', None)

      app.logger.info(f"AdminUserController#get START - Request received - userAgent={request.user_agent.string}")

      try: 
          product = self.productValidator.validate_product_exist(product_id)

          app.logger.info(f"AdminUserController#get SUCCESS - Product retrieved - productId={product.id} adminUserId={admin_user_id}")

          return jsonify(data=product.serialize())
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
          error_message = str(assertionError)
          app.logger.error(f'AdminUserController#get FAILURE - Can not get categories - reason={error_message}')
          return abort(400, message=error_message)

    def post(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminUserController#post START - Request received - userAgent={request.user_agent.string}")

      try: 
          self.userValidator.validate_create_new_user(request.json)

          user = self.userService.create_user(request.json)
          print(user)
          app.logger.info(f"AdminUserController#post SUCCESS - User retrieved - userId={user['id']}")

          return jsonify(data=user)
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
          error_message = str(assertionError)
          app.logger.error(f'AdminUserController#post FAILURE - Can not create product - reason={error_message}')
          return abort(400, message=error_message)

    # def patch(self):
    #   if not request.is_json:
    #     return abort(400, message=messages['missing_json'])

    #   app.logger.info(f"AdminUserController#patch START - Request received - userAgent={request.user_agent.string}")

    #   try: 
    #       product = self.productValidator.validate_update_product(request.json)

    #       product = self.productService.update(request.json, product)

    #       app.logger.info(f"AdminUserController#patch SUCCESS - Product retrieved - productId={product.id}")

    #       return jsonify(data=product.serialize())
    #   except ValueRequiredException as vex:
    #       return abort(400, message=str(vex))
    #   except AssertionError as assertionError:
    #       error_message = str(assertionError)
    #       app.logger.error(f'AdminUserController#patch FAILURE - Can not create product - reason={error_message}')
    #       return abort(400, message=error_message)

    # def delete(self):
    #   if not request.is_json:
    #     return abort(400, message=messages['missing_json'])

    #   app.logger.info(f"AdminUserController#delete START - Request received - userAgent={request.user_agent.string}")

    #   try: 
    #       product = self.productValidator.validate_product_exist(request.json.get('product_id', None))

    #       product = self.productService.delete_product(product)

    #       app.logger.info(f"AdminUserController#delete SUCCESS - Product retrieved - productId={product.id}")

    #       return '', 204
    #   except ValueRequiredException as vex:
    #       return abort(400, message=str(vex))
    #   except AssertionError as assertionError:
    #       error_message = str(assertionError)
    #       app.logger.error(f'AdminUserController#delete FAILURE - Can not create product - reason={error_message}')
    #       return abort(400, message=error_message)


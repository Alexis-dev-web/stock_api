# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.util.error_mesages import messages
from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from app.util.RequestExceptions import ValueRequiredException
from app.stock.service.CategoryService import CategoryService
from app.stock.service.CategoryValidator import CategoryValidator


class AdminCategoryController(Resource):

    method_decorators = {
        'post': [SecuredSystemMiddleware.web_user_authentication_required],
        'patch': [SecuredSystemMiddleware.web_user_authentication_required], 
        'delete': [SecuredSystemMiddleware.web_user_authentication_required]
    }

    def __init__(self):
      self.categoryValidator = CategoryValidator()
      self.categoryService = CategoryService()

    def post(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminCategoryController#post START - Request received - userAgent={request.user_agent.string}")

      try: 
        self.categoryValidator.validate_create_category(request.json)

        category = self.categoryService.create_category(request.json)

        app.logger.info(f"AdminCategoryController#post SUCCESS - Category created - categoryId={category.id} adminUserId={request.json.get('admin_user_id')}")

        return jsonify(data=category.serialize())
      except ValueRequiredException as vex:
          return abort(400, message=str(vex))
      except AssertionError as assertionError:
        error_message = str(assertionError)
        app.logger.error(f'AdminCategoryController#post FAILURE - Can not create category - reason={error_message}')
        return abort(400, message=error_message)

  
    def patch(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminCategoryController#patch START - Request received - userAgent={request.user_agent.string}")

      try: 
        category = self.categoryValidator.validate_update_category(request.json)

        category = self.categoryService.update_category(request.json, category)

        app.logger.info(f"AdminCategoryController#patch SUCCESS - Category updated - categoryId={category.id} adminUserId={request.json.get('admin_user_id')}")

        return jsonify(data=category.serialize())
      except ValueRequiredException as vex:
        return abort(400, message=str(vex))
      except AssertionError as assertionError:
        error_message = str(assertionError)
        app.logger.error(f'AdminCategoryController#patch FAILURE - Can not update category - reason={error_message}')
        return abort(400, message=error_message)

    def delete(self):
      if not request.is_json:
        return abort(400, message=messages['missing_json'])

      app.logger.info(f"AdminCategoryController#patch START - Request received - userAgent={request.user_agent.string}")

      try: 
        category = self.categoryValidator.validate_category_exist(request.json)

        category = self.categoryService.delete_category(category)

        app.logger.info(f"AdminCategoryController#patch SUCCESS - Category delete - categoryId={category.id} adminUserId={request.json.get('admin_user_id')}")

        return jsonify(data=category.serialize())
      except ValueRequiredException as vex:
        return abort(400, message=str(vex))
      except AssertionError as assertionError:
        error_message = str(assertionError)
        app.logger.error(f'AdminCategoryController#patch FAILURE - Can not delete category - reason={error_message}')
        return abort(400, message=error_message)

# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from app.util.RequestExceptions import ValueRequiredException
from app.stock.service.CategoryService import CategoryService


class AdminCategoriesController(Resource):

    method_decorators = {
        'get': [SecuredSystemMiddleware.web_user_authentication_required]
    }

    def __init__(self):
        self.categoryService = CategoryService()

    def get(self):
        admin_user_id = request.args.get('admin_user_id', None)

        app.logger.info(f"AdminCategoriesController#get START - Request received - userAgent={request.user_agent.string}")

        try: 
            # self.adminAuthValidator.validate_admin_request(request.args)

            categories = self.categoryService.get_all()

            app.logger.info(f"AdminCategoriesController#get SUCCESS - Categories retrieved - countCategories={len(categories)} adminUserId={admin_user_id}")

            return jsonify(data=categories)
        except ValueRequiredException as vex:
            return abort(400, message=str(vex))
        except AssertionError as assertionError:
            error_message = str(assertionError)
            app.logger.error(f'AdminCategoriesController#get FAILURE - Can not get categories - reason={error_message}')
            return abort(400, message=error_message)


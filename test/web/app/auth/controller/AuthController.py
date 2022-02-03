from flask import request, jsonify
from flask_restful import Resource, abort

from app import app
from app.util.error_mesages import messages
from app.user.service.UserService import UserService
from app.user.service.UserValidator import UserValidator


class AuthController(Resource):

    def __init__(self):
      self.userValidator = UserValidator()
      self.userService = UserService()

    def post(self):
      if not request.is_json:
          return abort(400, message=messages['missing_json'])

      app.logger.info(f"AuthController#post START - Login event received - userAgent={request.user_agent.string}")

      try:
          user = self.userValidator.validate_web_login_params(request.json)
          api_tokens = self.authService.generate_web_user_authentication_tokens(user.id)
          
          user = user.serialize()
          user["api_tokens"] = api_tokens
          app.logger.info(f"AuthController#post INFO - Login success - userId={user['id']}")
      
          return jsonify(data=user)
      except Exception as e:
          error_message = str(e)
          app.logger.error(f'AuthController#post FAILURE - Can not login - reason={error_message}')
          return abort(400, message=error_message)
            
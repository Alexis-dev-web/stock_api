from functools import wraps
from flask import request
from flask_restful import abort

from app import app
from app.providers.JWTProvider import JWTProvider
from app.auth.AuthMiddlewareValidator import validate_admin_user_token


class SecuredSystemMiddleware:
    
  @staticmethod
  def validate_token_admin(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          
          if not request.headers.get("authorization"):
              return abort(401, message="Authorization header required")

          if not request.headers["authorization"]:
              return abort(401, message="Authorization required")
          
          admin_token = request.headers.get("authorization")
          jwt_provider = JWTProvider()
          user_payload = jwt_provider.parser_user_with_expiration_time(admin_token)

          if not user_payload or not user_payload["userId"]:
              return abort(401, message="Token has expired", reason="TOKEN_NOT_VALID")

          try:
              validate_admin_user_token(user_payload)
          except AssertionError as assertionError:
              error_message = str(assertionError)
              app.logger.error(f"SecuredSystemMiddleware#validate_token_admin FAILURE - Validation error - exception={error_message}")
              return abort(400, message=error_message)

          return func(*args, **kwargs)

      return wrapper

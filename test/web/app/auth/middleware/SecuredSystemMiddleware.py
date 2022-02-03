from functools import wraps
from flask import request
from flask_restful import abort

from app import app
from app.providers.JWTProvider import JWTProvider
from app.auth.AuthMiddlewareValidator import validate_admin_user_token


class SecuredSystemMiddleware:
    
  @staticmethod
  def web_user_authentication_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.headers.get("authorization"):
            return abort(401, message="Authorization required")

        if not request.headers["authorization"]:
            return abort(401, message="Authorization required")
        
        user_token = request.headers.get("authorization")
        jwt_provider = JWTProvider()
        user_payload = jwt_provider.parser_user_with_expiration_time(user_token)

        if not user_payload or not user_payload["userId"]:
            return abort(401, message="Token has expired")

        try:
            validate_admin_user_token(user_token, user_payload)
        except Exception as e:
            error_message = str(e)
            app.logger.error(f"UserAuthMiddleware#web_user_authentication_required FAILURE - Validation error - reason={error_message}")
            return abort(401, message=error_message)

        return func(*args, **kwargs)

    return wrapper

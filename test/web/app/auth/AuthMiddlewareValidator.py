from app.util.error_mesages import messages
from app.user.model.UserRepository import UserRepository
from app.auth.model.UserApiTokenRepository import UserApiTokenRepository


def validate_admin_user_token(user_token, user_payload):
  web_user_api_token_repository = UserApiTokenRepository()
  user_repository = UserRepository()

  web_user_api_token = web_user_api_token_repository.get_by_api_token(user_token)
  if not web_user_api_token:
      raise AssertionError("Token not valid")

  user = user_repository.get_by_id(user_payload["userId"])
  if not user:
      raise AssertionError("User does not exist")
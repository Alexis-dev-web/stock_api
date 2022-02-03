from app.util.error_mesages import messages
from app.user.model.UserRepository import UserRepository
from app.auth.model.LoginRepository import LoginRepository


def validate_admin_user_token(user_payload):
  user_repository = UserRepository()
  login_repository = LoginRepository()

  user = user_repository.get_by_id(user_payload["userId"])
  if not user:
    raise AssertionError(messages['user_not_exist'])
  
  login = login_repository.get_by_email(user_payload["email"])
  if not login:
    raise AssertionError(messages['cradentials_not_exist'])

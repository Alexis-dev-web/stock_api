from app.util.RequestExceptions import ValueRequiredException
from app.util.error_mesages import messages
from werkzeug.security import check_password_hash

from app.user.model.UserRepository import UserRepository
from app.user.model.User import GenderType, Profile
from app.auth.model.LoginRepository import LoginRepository


class UserValidator:

  def __init__(self) -> None:
    self.userRepository = UserRepository()
    self.loginRepository = LoginRepository()

  def validate_create_new_user(self, json_body):
    email = json_body.get('email', None)
    admin_user_id = json_body.get('admin_user_id', None)

    if not email:
      raise ValueRequiredException(messages['email_required'])

    user_email = self.loginRepository.get_by_email(email)
    if user_email:
      raise AssertionError(messages['email_take'])

    self.validate_general_user(json_body)

  def validate_user_exist(self, json_body):
    user_id = json_body.get('user_id', None)

    if not user_id:
      raise ValueRequiredException(messages['user_id_required'])

    user = self.userRepository.get_by_id(user_id)
    if not user:
      raise AssertionError(messages['user_not_exist'])

    return user

  def validate_general_user(self, json_body):
    name = json_body.get('name', None)
    last_name = json_body.get('last_name', None)
    gender = json_body.get('gender', None)
    profile = json_body.get('profile', None)
    if not name:
      raise ValueRequiredException(messages['name_required'])

    if not last_name:
      raise ValueRequiredException(messages['last_name_required'])

    if not gender:
      raise ValueRequiredException(messages['gender_required'])

    try:
      GenderType(gender)
    except:
      raise AssertionError(messages['gender_invalid'])

    if profile and not Profile(profile):
      raise AssertionError(messages['profile_invalid'])

  def validate_update_user(self, json_body):
    user = self.validate_user_exist(json_body)
    
    self.validate_general_user(json_body)

    return user

  def validate_web_login_params(self, json_request):
    email = json_request.get("email", None)
    password = json_request.get("password", None)

    if not email:
        raise ValueRequiredException(messages['email_required'])
    
    if not password:
        raise ValueRequiredException(messages['password_required'])

    login = self.loginRepository.get_by_email(email)
    if not login:
        raise AssertionError(messages['user_not_exist'])
    
    if not check_password_hash(login.password, password):
        raise AssertionError(messages['credentials_not_match'])
    
    if not login.email_confirmed:
        raise AssertionError(messages['verify_email'])

    user = self.userRepository.get_by_id(login.user_id)
    if not user:
        raise AssertionError(messages['user_not_exist'])

    return user
    
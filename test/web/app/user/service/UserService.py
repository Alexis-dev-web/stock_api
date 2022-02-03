from urllib import response
from app.user.model.UserRepository import User, UserRepository
from app.user.model.User import GenderType, Profile
from app.BaseModel import Login
from app.auth.model.LoginRepository import LoginRepository
from app.util.utils import generate_random_password


class UserService:

  def __init__(self) -> None:
    self.userRepository = UserRepository()
    self.loginRepository = LoginRepository()

  def create_user(self, json_body):
    name = json_body.get('name')
    last_name = json_body.get('last_name')
    gender = json_body.get('gender')
    profile = json_body.get('profile', None)
    email = json_body.get('email')

    user = User()
    user.name = name
    user.last_name = last_name
    user.gender = GenderType(gender)
    user.profile = profile if not profile else Profile(profile)
    user = self.userRepository.save(user)

    login = Login(email=email, password=generate_random_password(8))
    login.user_id = user.id
    login = self.loginRepository.save(login)

    user = user.serialize()
    user['email'] = login.email

    return user

  def update_user(self, json_body, user):
    name = json_body.get('name')
    last_name = json_body.get('last_name')
    gender = json_body.get('gender')
    profile = json_body.get('profile', None)

    user.name = name
    user.last_name = last_name
    user.gender = GenderType(gender)
    user.profile = Profile(profile)

    return self.userRepository.update(user)

  def activate_or_deactivate_user(self, user):
    user.active = not user.activate
    return self.userRepository.update(user)

  def change_password(self, json_body, login):
    login.password = json_body.get('password')
    return self.loginRepository.update(login)

  def response_user_with_email(self, user):
    response = user.User.serialize()
    response['email'] = user.email
    return response

  def delete_user(self, user):
    login = self.loginRepository.get_by_user_id(user.User.id)
    return self.loginRepository.delete(login)

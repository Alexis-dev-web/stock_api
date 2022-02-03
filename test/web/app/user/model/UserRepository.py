from app import db

from app.user.model.User import User
from app.BaseModel import Login


class UserRepository:

  def get_by_id(self, user_id) -> User:
    return User.query.get(user_id)

  def get_all(self) -> list:
    return User.query.all()

  def save(self, user) -> User:
    db.session.add(user)
    db.session.commit()
    return user

  def update(self, user) -> User:
    db.session.commit()
    return user

  def get_by_id_with_email(self, user_id):
    return User.query.join(Login, User.id == Login.user_id)\
      .add_columns(Login.email)\
      .filter(User.id==user_id).first()
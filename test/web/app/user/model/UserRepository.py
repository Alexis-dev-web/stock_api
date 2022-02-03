from app import db
from sqlalchemy import func

from app.user.model.User import User


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

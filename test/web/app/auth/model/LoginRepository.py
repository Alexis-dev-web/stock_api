from app import db
from sqlalchemy import func

from app.BaseModel import Login


class LoginRepository:

  def get_by_id(self, login_id) -> Login:
    return Login.query.get(login_id)

  def get_all(self) -> list:
    return Login.query.all()

  def save(self, login) -> Login:
    db.session.add(login)
    db.session.commit()
    return login

  def update(self, Login) -> Login:
    db.session.commit()
    return Login

  def delete(self, login) -> Login:
    login.active = False
    db.session.commit()

    return login

  def get_by_user_id(self, user_id) -> Login:
    return Login.query.filter_by(user_id=user_id).first()

  def get_by_email(self, email) -> Login:
    return Login.query.filter_by(email=email).first()

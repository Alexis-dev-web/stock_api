from app import db
from sqlalchemy import func

from app.user.model.Logs import Logs


class LogsRepository:

  def get_by_id(self, log_id) -> Logs:
    return Logs.query.get(log_id)

  def get_all(self) -> list:
    return Logs.query.all()

  def save(self, logs) -> Logs:
    db.session.add(logs)
    db.session.commit()
    return logs

  def delete(self, Logs) -> Logs:
    Logs.active = False
    db.session.commit()

    return Logs

  def get_by_product_id(self, product_id) -> Logs:
    return Logs.query.filter_by(product_id=product_id).first()

from app import db
from sqlalchemy import func

from app.stock.model.Category import Category


class CategoryRepository:

  def get_by_id(self, category_id) -> Category:
    return Category.query.get(category_id)

  def get_all(self) -> list:
    return Category.query.all()

  def save(self, category) -> Category:
    db.session.add(Category)
    db.session.commit()
    return category

  def update(self, category) -> Category:
    db.session.commit()
    return category

  def delete(self, category) -> bool:
    try:
      db.session.delete(category)
      db.session.commit()
      return True
    except:
      db.session.rollback()
      return False

  def get_by_name(self, name):
    return Category.query.filter_by(name=name).first()

  def get_by_name_and_diferent_id(self, name, category_id):
    return Category.quary.filter_by(name=name)\
      .filter(Category.id != category_id).first()

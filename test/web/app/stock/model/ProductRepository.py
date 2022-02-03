from app import db
from sqlalchemy import func

from app.stock.model.Product import Product


class ProductRepository:

  def get_by_id(self, product_id) -> Product:
    return Product.query.get(product_id)

  def get_all(self) -> list:
    return Product.query.all()

  def save(self, product) -> Product:
    db.session.add(product)
    db.session.commit()
    return product

  def update(self, product) -> Product:
    db.session.commit()
    return product

  def delete(self, product) -> bool:
    try:
      db.session.delete(product)
      db.session.commit()
      return True
    except:
      db.session.rollback()
      return False

  def get_active_by_category_id(self, category_id):
    return Product.query.filter_by(category_id=category_id, active=True).all()

  def get_by_category_id(self, category_id):
    return Product.query.filter_by(category_id=category_id).all()

  def get_by_name(self, name):
    return Product.query.filter_by(name=name).first()

  def get_by_name_and_diferent_id(self, name, product_id):
    return Product.quary.filter_by(name=name)\
      .filter(Product.id != product_id).first()

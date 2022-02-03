from sqlalchemy import func
from app import db

import uuid
import enum


class Product(db.Model):
  __tablename__ = "Product"

  id = db.Column(db.String(255), primary_key=True)
  name = db.Column(db.String(50), unique=True, nullable=False)
  price = db.Column(db.Float(), nullable=False)
  description = db.Column(db.String(500), nullable=True)
  quantity = db.Column(db.Integer(), nullable=False, default=0)
  active = db.Column(db.Boolean(), default=True, nullable=True)
  category_id = db.Column(db.String(255), db.ForeignKey('Category.id'), nullable=False)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __init__(self):
      self.id = str(uuid.uuid4())
  
  def serialize(self):
      return {
          'id': self.id, 
          'name': self.name,
          'descriptiom': self.description,
          'price': self.price,
          'quantity': self.quantity,
          'active': self.active,
          'category_id': self.category_id,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }

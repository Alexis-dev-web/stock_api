from itertools import product
from sqlalchemy import func
from app import db
import uuid
import enum


class Logs(db.Model):
  __tablename__ = "Logs"

  id = db.Column(db.String(255), primary_key=True)
  product_id = db.Column(db.String(255), db.ForeignKey('Category.id'), nullable=False)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())

  def __init__(self):
      self.id = str(uuid.uuid4())
  
  def serialize(self):
      return {
          'id': self.id, 
          'event': self.event.name,
          'product_id': self.product_id,
          'created_at': self.created_at
      }

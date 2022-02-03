from sqlalchemy import func
from app import db
import uuid


class Category(db.Model):
  __tablename__ = "Category"

  id = db.Column(db.String(255), primary_key=True)
  name = db.Column(db.String(255), unique=True, nullable=False)
  description = db.Column(db.String(500), nullable=True)
  active = db.Column(db.Boolean(), default=True, nullable=True)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __init__(self):
      self.id = str(uuid.uuid4())

  def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'description': self.description,
          'active': self.active,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }

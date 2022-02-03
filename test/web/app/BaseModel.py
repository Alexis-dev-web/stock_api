from email.policy import default
from enum import unique
from sqlalchemy import func
from app import db
import uuid


class Login(db.Model):
  __tablename__ = "Login"

  id = db.Column(db.String(255), primary_key=True)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=True)
  # confirmation_code = db.Column(db.String(255), nullable=True)
  # confirmed = db.Column(db.Boolean(), default=False, nullable=False)
  active = db.Column(db.Boolean(), default=True, nullable=False)
  user_id = db.Column(db.String(255), db.ForeignKey('Users.id'), unique=True, nullable=False)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __init__(self, email=None, password=None):
      self.email = email
      self.password = password
      self.id = str(uuid.uuid4())
  
  def serialize(self):
      return {
          'id': self.id, 
          'email': self.email,
          # 'confirmation_code': self.confirmation_code,
          # 'confirmed': self.confirmed,
          'user_id': self.user_id,
          'active': self.active,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }

from email.policy import default
from sqlalchemy import func
from app import db
import uuid
import enum


class GenderType(enum.Enum):
  MALE = 'MALE'
  FEMALE = 'FEMALE'


class Profile(enum.Enum):
  ADMIN = 'ADMIN'
  OTHER = 'OTHER'


class User(db.Model):
  __tablename__ = "User"

  id = db.Column(db.String(255), primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  gender = db.Column(db.Enum(GenderType))
  profile = db.Column(db.Enum(Profile), default=Profile.ADMIN)
  created_at  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
  updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __init__(self):
      self.id = str(uuid.uuid4())
  
  def serialize(self):
      return {
          'id': self.id, 
          'name': self.name,
          'last_name': self.last_name,
          'gender': self.gender.name if self.gender else None,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }

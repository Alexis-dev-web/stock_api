from app import db
import uuid


class UserApiToken(db.Model):
    __tablename__ = "UserApiToken"

    id = db.Column(db.String(255), primary_key=True)
    api_token = db.Column(db.String(255), nullable=False)
    refresh_token = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), db.ForeignKey('User.id'), nullable=False)

    def __init__(self):
        self.id = str(uuid.uuid4())

    def serialize(self):
        return {
            'id': self.id,
            'api_token': self.api_token,
            'refresh_token': self.refresh_token,
            'user_id': self.user_id
        }
        
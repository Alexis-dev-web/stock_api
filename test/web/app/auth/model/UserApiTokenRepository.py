from app import db
from app.auth.model.UserApiToken import UserApiToken


class UserApiTokenRepository:
    
    def save(self, web_user_api_token) -> UserApiToken:
        db.session.add(web_user_api_token)
        db.session.commit()
        return web_user_api_token
    
    def delete(self, web_user_api_token) -> bool:
        try:
            db.session.delete(web_user_api_token)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def update(self, web_user_api_token) -> UserApiToken:
        db.session.commit()
        return web_user_api_token

    def get_by_id(self, web_user_api_token_id) -> UserApiToken:
        return UserApiToken.query.get(web_user_api_token_id)
    
    def get_by_user_id(self, user_id) -> UserApiToken:
        return UserApiToken.query.filter_by(user_id=user_id).first()
    
    def get_by_api_token(self, web_user_api_token) -> UserApiToken:
        return UserApiToken.query.filter_by(api_token=web_user_api_token).first()

    def get_by_refresh_token(self, web_user_api_token) -> UserApiToken:
        return UserApiToken.query.filter_by(refresh_token=web_user_api_token).first()
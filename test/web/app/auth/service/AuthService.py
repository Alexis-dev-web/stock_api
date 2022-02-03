from app.providers.JWTProvider import JWTProvider
import datetime

from app.user.model.UserRepository import UserRepository
from app.auth.model.UserApiTokenRepository import UserApiToken, UserApiTokenRepository
from app.user.model.User import db
from app import app


class AuthService:

    def __init__(self):
        self.jwtProvider = JWTProvider()
        self.EXPIRATION_DAYS = 1
        self.EXPIRATION_HOURS = 12
        self.REFRESH_EXPIRATION_DAYS = 30  # 30 dias
        self.userRepository = UserRepository()
        self.userApiTokenRepository = UserApiTokenRepository()
        self.EXPIRE_IN_HOUR = 1

    def generate_web_user_authentication_tokens(self, user_id):
        try:
            token = self.jwtProvider.generate_user_with_expiration_days(user_id, self.EXPIRATION_DAYS)
            refresh_token = self.jwtProvider.generate_user_with_expiration_days(user_id, self.REFRESH_EXPIRATION_DAYS)

            app.logger.info(f"AuthService#generate_web_user_authentication_tokens SUCCESS - User auth tokens created - userId={user_id}")

            web_user_api_token = self.userApiTokenRepository.get_by_user_id(user_id)

            if not web_user_api_token:
                web_user_api_token = UserApiToken()
                web_user_api_token.user_id = user_id

            web_user_api_token.api_token = token
            web_user_api_token.refresh_token = refresh_token

            self.userApiTokenRepository.save(web_user_api_token)

            return web_user_api_token.serialize()
        except Exception as e:
            app.logger.info(f"AuthService#generate_web_user_authentication_tokens FAILED - Can not create auth tokens - reason={e}")
            return None

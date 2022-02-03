import hashlib
import math
import os
import time
import jwt
import datetime
from app import app


class JWTProvider:
    """
        Class to create and verify a signed token, used for API access
    """

    def __init__(self):
        self.JWT_SECRET = os.environ.get("JWT_SECRET")
        self.ALGORITHM = os.environ.get("ALGORITHM")

    def generate_user_with_expiration_date(self, user_id, expiration_time):
        """
            Create a signed token with expiration date

            Parameters
            ----------
            user_id : str
                The user identifier
            expiration_time : datetime
                Token expiration time
        """

        claim_data = {
            'userId': user_id,
            'exp': expiration_time
        }

        return self.generate_jwt(claim_data)

    def generate_user_email_token(self, email):
        claim_data = {
            'email': email
        }

        return self.generate_jwt(claim_data)

    def generate_jwt(self, claim_data):
        """
            Create signed token

            Returns
            ----------
            str
            utf-8 string token decoded

        """
        print(jwt.encode(claim_data, self.JWT_SECRET, algorithm=self.ALGORITHM))
        return jwt.encode(claim_data, self.JWT_SECRET, algorithm=self.ALGORITHM)

    def generate_user_with_expiration_hours(self, user_id, expiration_hours):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=expiration_hours)

        return self.generate_user_with_expiration_date(user_id, expiration_time)

    def generate_user_with_expiration_minutes(self, user_id, expiration_minutes):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)

        return self.generate_user_with_expiration_date(user_id, expiration_time)

    def generate_user_with_expiration_days(self, user_id, expiration_days):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=expiration_days)

        return self.generate_user_with_expiration_date(user_id, expiration_time)

    def parser_user_with_expiration_time(self, token):
        """
            Verify the token

            Returns
            ----------
            Dic
            A dictionary {'key' : value} if the "token" is valid
        """
        try:
            return jwt.decode(token, self.JWT_SECRET, algorithms=[self.ALGORITHM])
        except jwt.ExpiredSignatureError:
            app.logger.error("JWTProvider#parser_user_with_expiration_time ERROR - the token has expired -")
            return None
        except Exception as e:
            app.logger.error("JWTProvider#parser_user_with_expiration_time the token error error:%s" % str(e))
            return None

    
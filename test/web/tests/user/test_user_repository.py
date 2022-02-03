import pytest
import uuid

from app import db
from datetime import datetime, timedelta
from tests.BaseCase import BaseCase
from datetime import datetime
from app.user.model.User import User, GenderType, Profile
from app.user.model.UserRepository import UserRepository
from app.auth.model.LoginRepository import LoginRepository, Login


class TestUserRepository(BaseCase):
    
    def build_test_user(self):
        user = User("Austin Post")
        return user

    def build_test_user_login(self, user_id, email):
        login = Login()
        login.email = email
        login.user_id = user_id

        return login
    
    def 


from ..Repository.repo import *
from ..Models.models import *
from ..Exceptions.exception import *


class UserService():

    def __init__(self):
        self.user = Users()

    def add_user(self, name, phone_no, email, password):
        user = self.user.get_user_by_phone(phone_no)
        if len(user) != 0:
            raise UserAlreadyExists('User Exists')
        else:
            user = User()
            user.name = name
            user.email = email
            user.phoneNumber = phone_no
            user.password = password








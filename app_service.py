''' Simple service that serves user data '''

import json

class AppService:
    ''' Service class for working with user data '''

    def __init__(self, file_name):
        self.users = json.load(open(file_name))

    def get_users(self):
        return self.users

    def get_user(self, user_id):
        return self.users.get(str(user_id), 'World')

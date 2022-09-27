''' Simple Flask program that exposes an endpoint to greet the users '''

from flask import Flask
from app_service import AppService

app = Flask(__name__)
appService = AppService('users.json')

@app.route('/<int:user_id>')
def greet(user_id):
    '''Takes user_id parameter and returns a greeting message'''
    user_name = appService.get_user(user_id)
    return f'Hello, {user_name}!'

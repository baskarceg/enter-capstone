import os
from flask import Flask
from models import setup_db
from flask_cors import CORS
from models import Person

from auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    @requires_auth('get:drinks-detail')
    def get_greeting(payload):
        excited = 'true'
        #persons = Person.query.all()
        #print(persons)
        greeting = "Fuck You"
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

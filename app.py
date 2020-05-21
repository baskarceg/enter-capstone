import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS

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

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        "success" : False,
        "error" : 404,
        "message" : "Not Found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
        "success" : False,
        "error" : 405,
        "message" : "Method Not Allowed"
        }), 405

    @app.errorhandler(400)
    def method_not_allowed(error):
        return jsonify({
        "success" : False,
        "error" : 400,
        "message" : "Bad Request"
        }), 400

    @app.errorhandler(422)
    def method_not_allowed(error):
        return jsonify({
        "success" : False,
        "error" : 422,
        "message" : "Unprocessable Entity"
        }), 422

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify({
                        "success": False,
                        "error": e.status_code,
                        "message": e.error
                        }), e.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

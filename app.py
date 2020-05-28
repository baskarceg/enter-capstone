import os
from flask import Flask, jsonify, request, abort
from models import setup_db
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from models import Movie, Actor

from auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        return "Welcome to Capstone Casting Agency"



    @app.route('/movies')
    @requires_auth('get:movies')
    def get_all_movies(payload):
        try:
            movies = Movie.query.order_by(Movie.id).all()
            movies_list = [ movie.format() for movie in movies ]
            return jsonify({
            'movies_list' : movies_list,
            'success' : True
            })
        except AttributeError:
            abort(400)

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_all_actors(payload):
        try:
            actors = Actor.query.order_by(Actor.id).all()
            actors_list = [ actor.format() for actor in actors ]
            return jsonify({
            'actors_list' : actors_list,
            'success' : True
            })
        except AttributeError:
            abort(400)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_new_movie(payload):
        body=request.get_json()

        try:
            if body is None:
                abort(400)
            else:
                movie = Movie(body["title"], body["release_date"])
                movie.insert()
                return jsonify({
                'success' : True
                })
        except IntegrityError:
            abort(400)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_new_actor(payload):
        body=request.get_json()
        try:
            if body is None:
                abort(400)
            else:
                actor = Actor(body["name"], body["age"],
                body["gender"])
                actor.insert()
                return jsonify({
                'success' : True
                })
        except IntegrityError:
            abort(400)

    @app.route('/movies/<movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_a_movie(payload, movie_id):
        movie = Movie.query.filter(Movie.id==movie_id).one_or_none()

        if movie is None:
            abort(404)

        else :
            movie.delete()
            return jsonify({
            'success' : True
            })

    @app.route('/actors/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_an_actor(payload, actor_id):
        actor = Actor.query.filter(Actor.id==actor_id).one_or_none()

        if actor is None:
            abort(404)

        else :
            actor.delete()
            return jsonify({
            'success' : True
            })

    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def modify_a_movie(payload, movie_id):
        movie = Movie.query.filter(Movie.id==movie_id).one_or_none()

        body=request.get_json()

        try:
            if body is None:
                abort(400)

            else:

                if "title" in body:
                    movie.title = body["title"]

                if "release_date" in body:
                    movie.release_date = body["release_date"]

                movie.update()

                return jsonify({
                'movie' : movie.format(),
                'success' : True
                })

        except IntegrityError:
            abort(400)

    @app.route('/actors/<actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def modify_an_actor(payload, actor_id):
        actor = Actor.query.filter(Actor.id==actor_id).one_or_none()

        body=request.get_json()

        try:
            if body is None:
                abort(400)

            else:

                if "name" in body:
                    actor.name = body["name"]

                if "age" in body:
                    actor.age = body["age"]

                if "gender" in body:
                    actor.gender = body["gender"]

                actor.update()

                return jsonify({
                'actor' : actor.format(),
                'success' : True
                })

        except IntegrityError:
            abort(400)

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

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, db, Actor, Movie

EXEC_TOKEN = os.environ['EXEC_TOKEN']
ASSIS_TOKEN = os.environ['ASSIS_TOKEN']
DIR_TOKEN = os.environ['DIR_TOKEN']
TOKEN_INVALID = os.environ['TOKEN_INVALID']
TOKEN_EXPIRED = os.environ['TOKEN_EXPIRED']


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432',  self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


    """
    Test case for GET '/movies' with Casting Assistant Role
    """
    def test_get_movies_cast_assist(self):
        result = self.client().get('/movies',
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('movies_list' in data)

    """
    Test case for GET '/movies' with Casting Director Role
    """

    def test_get_movies_cast_direct(self):
        result = self.client().get('/movies',
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('movies_list' in data)

    """
    Test case for GET '/movies' with Executive Producer Role
    """

    def test_get_movies_exec_prod(self):
        result = self.client().get('/movies',
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('movies_list' in data)

    """
    Test case for GET '/actors' with Casting Assistant Role
    """

    def test_get_actors_cast_assist(self):
        result = self.client().get('/actors',
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('actors_list' in data)

    """
    Test case for GET '/actors' with Casting Director Role
    """

    def test_get_actors_cast_direct(self):
        result = self.client().get('/actors',
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('actors_list' in data)

    """
    Test case for GET '/actors' with Executive Producer Role
    """

    def test_get_actors_exec_prod(self):
        result = self.client().get('/actors',
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('actors_list' in data)

    """
    Test case for POST '/movies' with Casting Assistant Role
    """

    def test_create_new_movies_cast_assist(self):
        result = self.client().post('/movies',
        json = {'title' : 'Marudhanayagam',
        'release_date': '2002-12-05'} ,
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for POST '/movies' with Casting Director Role
    """

    def test_create_new_movies_cast_direct(self):
        result = self.client().post('/movies',
        json = {'title' : 'Jimmy',
        'release_date': '1990-03-10'},
        headers={"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for POST '/movies' with Executive Producer Role
    """

    def test_create_new_movies_exec_prod(self):
        result = self.client().post('/movies',
        json = {'title' : 'Marudhanayagam',
        'release_date': '2002-12-05'} ,
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    """
    Test case for POST '/actors' with Casting Assistant Role
    """

    def test_create_new_actors_cast_assist(self):
        result = self.client().post('/actors',
        json = {'name' : 'Vijay Sethupathi',
        'age': 40 , 'gender' : 'Male'},
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for POST '/actors' with Casting Director Role
    """

    def test_create_new_actors_cast_direct(self):
        result = self.client().post('/actors',
        json = {'name' : 'Vijay Sethupathi',
        'age': 40 , 'gender' : 'Male'},
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    """
    Test case for POST '/actors' with Executive Producer Role
    """

    def test_create_new_actors_exec_prod(self):
        result = self.client().post('/actors',
        json = {'name' : 'Vijay Sethupathi',
        'age': 40 , 'gender' : 'Male'},
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    """
    Test case for PATCH '/actors' with Casting Assistant Role
    """

    def test_patch_actors_cast_assist(self):
        result = self.client().patch('/actors/1',
        json = {'gender' : 'Female'},
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for PATCH '/actors' with Casting Director Role
    """

    def test_patch_actors_cast_direct(self):
        result = self.client().patch('/actors/1',
        json = {'gender' : 'Female'},
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(actor.gender,"Female")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        result = self.client().patch('/actors/1',
        json = {'gender' : 'Male'},
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(actor.gender,"Male")

    """
    Test case for PATCH '/actors' with Executive Producer Role
    """

    def test_patch_actors_exec_prod(self):
        result = self.client().patch('/actors/1',
        json = {'gender' : 'Female'},
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(actor.gender,"Female")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        result = self.client().patch('/actors/1',
        json = {'gender' : 'Male'} ,
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(actor.gender,"Male")

    """
    Test case for PATCH '/movies' with Casting Assistant Role
    """

    def test_patch_movies_cast_assist(self):
        result = self.client().patch('/movies/1',
        json = {'title' : 'Jingle Bells'},
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for PATCH '/movies' with Casting Director Role
    """

    def test_patch_movies_cast_direct(self):
        result = self.client().patch('/movies/1',
        json = {'title' : 'Jingle Bells'},
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(movie.title,"Jingle Bells")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        result = self.client().patch('/movies/1',
        json={'title' : 'Test Test'},
        headers={"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(movie.title,"Test Test")
        self.assertEqual(result.status_code, 200)

    """
    Test case for PATCH '/movies' with Executive Producer Role
    """

    def test_patch_movies_exec_prod(self):
        result = self.client().patch('/movies/1',
        json = {'title' : 'Jingle Bells'},
        headers={"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(movie.title,"Jingle Bells")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        result = self.client().patch('/movies/1',
        json = {'title' : 'Test Test'},
        headers={"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(movie.title,"Test Test")
        self.assertEqual(result.status_code, 200)


    """
    Test case for DELETE '/movies' with Casting Assistant Role
    """

    def test_delete_movies_cast_assist(self):
        result = self.client().delete("/movies/3",
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for DELETE '/movies' with Casting Director Role
    """

    def test_delete_movies_cast_direct(self):
        result = self.client().delete("/movies/3",
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for DELETE '/movies' with Executive Producer Role
    """

    def test_delete_movies_exec_prod(self):
        result = self.client().delete("/movies/2",
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        movie= Movie.query.order_by(Movie.id.desc()).first()
        movie.id=2
        movie.update()

    """
    Test case for DELETE '/actors' with Casting Assistant Role
    """

    def test_delete_actors_cast_assist(self):
        result = self.client().delete("/actors/2",
        headers = {"Authorization": "Bearer {}".format(ASSIS_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)

    """
    Test case for DELETE '/actors' with Casting Director Role
    """

    def test_delete_actors_cast_direct(self):
        result = self.client().delete("/actors/2",
        headers = {"Authorization": "Bearer {}".format(DIR_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        actor = Actor.query.order_by(Actor.id.desc()).first()
        actor.id=2
        actor.update()

    """
    Test case for DELETE '/actors' with Executive Producer Role
    """

    def test_delete_actors_exec_prod(self):
        result = self.client().delete("/actors/3",
        headers = {"Authorization": "Bearer {}".format(EXEC_TOKEN)})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        actor = Actor.query.order_by(Actor.id.desc()).first()
        actor.id=3
        actor.update()


    """
    Test case for no Auth Header Error
    """

    def test_header_missing_error(self):
        result = self.client().get('/movies')
        data = json.loads(result.data)
        message = data['message']
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(message['code'],
        "authorization_header_missing")

    """
    Test case for Token Parse error
    """
    def test_unable_parse_token_error(self):
        result = self.client().get('/movies',
        headers={"Authorization": "Bearer {}".format(TOKEN_INVALID)})
        data = json.loads(result.data)
        message = data['message']
        self.assertEqual(result.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(message['description'],
        "Unable to parse authentication token.")

    """
    Test case for Token expired error
    """
    def test_token_expired_error(self):
        result = self.client().get('/movies',
        headers={"Authorization": "Bearer {}".format(TOKEN_EXPIRED)})
        data = json.loads(result.data)
        message = data['message']
        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(message['description'], "Token expired.")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

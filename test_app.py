import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, db

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432',  self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful
     operation and for expected errors.
    """
    def test_get_all_questions_success(self):
        self.assertEqual(1,2)
    # def test_get_all_questions_success(self):
    #     result = self.client().get('/questions')
    #     data = json.loads(result.data)
    #     total_questions = len(Question.query.all())
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['categories'])
    #     self.assertEqual(data['total_questions'], total_questions)
    #     self.assertEqual(data['current_category'], "All")
    #
    # def test_get_all_questions_404(self):
    #     result = self.client().get('/questions?page=2000')
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Not Found")
    #     self.assertEqual(data["error"], 404)
    #
    # def test_get_all_categories_success(self):
    #     result = self.client().get('/questions')
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['categories'])
    #
    #
    # def test_detele_specific_question_success(self):
    #     result = self.client().delete('/questions/10')
    #     data = json.loads(result.data)
    #     question = Question.query.filter(Question.id==10).one_or_none()
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(question, None)
    #
    #     db.engine.execute("INSERT INTO questions "+
    #     "(id,question, answer,"
    #     +" difficulty,category) VALUES (10,'Which "+
    #     "is the only team to play in every soccer "+
    #     "World Cup tournament?', 'Uruguay', 4 , 6)")
    #
    # def test_detele_specific_question_404(self):
    #     result = self.client().delete('/questions/1000')
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Not Found")
    #     self.assertEqual(data["error"], 404)
    #
    # def test_create_new_question_success(self):
    #     result = self.client().post('/questions',
    #     json={'question' : 'Test',
    #     'answer' : 'Test',
    #     'category' : 4,'difficulty' : 2})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    # def test_create_new_question_400(self):
    #     result = self.client().post('/questions',
    #     json={'question' : 'Test',
    #     'answer' : 'Test','category' : 11,'difficulty' : 2})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 400)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Bad Request")
    #     self.assertEqual(data["error"], 400)
    #
    # def test_create_new_question_success(self):
    #     result = self.client().post('/questions',
    #     json={'question':'Test',
    #     'answer':'Test',
    #     'category':4, 'difficulty':2})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    # def test_create_new_question_400(self):
    #     result = self.client().post('/questions',
    #     json={'question' : 'Test', 'answer' : 'Test',
    #     'category' : 1000, 'difficulty' : 2})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 400)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Bad Request")
    #     self.assertEqual(data["error"], 400)
    #
    # def test_search_questions_success(self):
    #     result = self.client().post('/questions/search',
    #     json={'searchTerm' : 'A'})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'], True)
    #
    # def test_search_questions_404(self):
    #     result = self.client().post('/questions/search',
    #     json={'searchTerm' : 'akjhdsk'})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Not Found")
    #     self.assertEqual(data["error"], 404)
    #
    # def test_play_quiz_success(self):
    #     quizCategory = {'type' : 'History', 'id':'4'}
    #     previousQuestions = []
    #     result = self.client().post('/quizzes',
    #     json={'quiz_category' : quizCategory,
    #     'previous_questions' : previousQuestions})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['question'])
    #
    # def test_play_quiz_400(self):
    #     quizCategory = {}
    #     previousQuestions = []
    #     result = self.client().post('/quizzes'
    #     , json={'quiz_category' : quizCategory,
    #     'previous_questions' : previousQuestions})
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 400)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Bad Request")
    #     self.assertEqual(data["error"], 400)
    #
    # def test_get_question_by_category_success(self):
    #     result = self.client().get('/categories/1/questions')
    #     data = json.loads(result.data)
    #     total_questions = len(Question.query.
    #     filter(Question.category==1).all())
    #
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertEqual(data['total_questions'], total_questions)
    #     self.assertEqual(data['current_category'], '1')
    #
    # def test_get_question_by_category_404(self):
    #     result = self.client().get('/categories/7/questions')
    #     data = json.loads(result.data)
    #
    #     self.assertEqual(result.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "Not Found")
    #     self.assertEqual(data["error"], 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

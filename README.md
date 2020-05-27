# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### PIP Dependencies

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

Create a database locally using the command

createdb capstone;

## Running the server

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Running the 'source setup.sh' command will setup the environmental variables


```
Endpoints
GET '/movies'
GET '/actors'
POST '/movies'
POST '/actors'
DELETE '/movies/<movie_id>'
DELETE '/actors/<actor_id>'
PATCH '/movies/<movie_id>'
PATCH '/actors/<actor_id>'


GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a list of questions, number of total questions, current category, categories based on the page number passed in the argument
- Request Arguments: page
- Returns:

categories - An object with a single key, categories, that contains a object of id: category_string key:value pairs

total_questions - the total number of questions in the database

current_category - The current category

questions - A list of question objects


If the page is within limits

{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": "All",
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 19
}

If Page is out of bounds

{
  "error": 404,
  "message": "Not Found",
  "success": false
}

DELETE '/questions/<question_id>'
- It deletes the question with the passed question ID
- Request Arguments: None
- Returns: Success as true if the question_id was present , 404 error if the question_id was not present

IF question_id is available

{
  "success": true
}

IF question_id is not available

{
  "error": 404,
  "message": "Not Found",
  "success": false
}


POST '/questions'
- Posts a new question to the database
- Request Arguments: None
- Request Body : contains the question and answer text, category, and difficulty score.
Example
{'question':'Test','answer':'Test','category':4,'difficulty':2}
- Returns: Returns Success or 400 error based on if the insert is successful

If success

{
  'success':True
}

If error

{
   "success":False,
   "error":400,
   "message":"Bad Request"
}

POST '/questions/search'

- It returns questions based on a search term. It returns all the questions questions for which the search term is a substring of the question.
- Request Arguments: None
- Request Body : contains the search_term
Example
{'searchTerm':'you'}
- Returns:

If success

questions - the list of objects that has the search term as the substring
total_questions - total number of questions that matches the criteria  

{
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 2
}

If failure

{
   "success":False,
   "error":400,
   "message":"Bad Request"
}

GET '/categories/<category_id>/questions'

- It returns questions based on the category
- Request Arguments: None
- Returns:

total_questions - the total number of questions in the database

current_category - The current category

questions - A list of question objects


If the page is within limits

{
  "current_category": "1",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Test",
      "category": 1,
      "difficulty": 1,
      "id": 24,
      "question": "Test"
    },
    {
      "answer": "Test",
      "category": 1,
      "difficulty": 1,
      "id": 25,
      "question": "Who am I"
    }
  ],
  "success": true,
  "total_questions": 5
}

If there is no questions in the category

{
  "error": 404,
  "message": "Not Found",
  "success": false
}

If the category is not available

{
   "success":False,
   "error":400,
   "message":"Bad Request"
}

POST '/quizzes'

- This endpoint is to get questions to play the quiz.
 This endpoint should take category and previous question parameters
 and return a random questions within the given category,
 if provided, and that is not one of the previous questions.
- Request Arguments: None
- Request Body : contains the search_term
Example
{'quiz_category': {'type':'History','id':'4'} ,'previous_questions':[]})
- Returns:

If success , it returns a question

{
  "question": {
    "answer": "George Washington Carver",
    "category": 4,
    "difficulty": 2,
    "id": 12,
    "question": "Who invented Peanut Butter?"
  },
  "success": true
}

If there is not questions remaining in the category it returns False

{
  "success": False
}

If the category is wrong it returns error


{
   "success":False,
   "error":400,
   "message":"Bad Request"
}

## Testing
To run the tests, run
```
dropdb capstone_test
createdb capstone_test
python test_app.py
```

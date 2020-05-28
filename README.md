# Capstone Casting Agency

The Casting Agency is a company that is responsible for creating movies and managing and assigning actors to those movies.

The purpose of this project is to create a system to simplify and streamline this process

The system consists of the following models

  - Movies with attributes title and release date
  - Actors with attributes name, age and gender

The system consists of the following endpoints

  - GET /actors and /movies
  - POST /actors and /movies
  - DELETE /actors and /movies
  - PATCH /actors and /movies

The system consists of the following Roles

  - Casting Assistant
      - Can view actors and movies

  - Casting Director
      - All permissions a Casting Assistant has and…
      - Add or delete an actor from the database
      - Modify actors or movies

  - Executive Producer
      - All permissions a Casting Director has and…
      - Add or delete a movie from the database


Live appication is hosted on Heroku in the below URL:
https://enter-capstone.herokuapp.com/

You can test the endpoints by importing the postman collection 'enter_capstone.json'

The Tokens for all three roles are available in the collection and also the setup.sh file

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


GET '/movies'
- Fetches a list of movies form the database
- Request Arguments: None
- Returns:
    - movies_list - A list of movie objects

- Sample Output

    {
        "movies_list": [
            {
                "id": 1,
                "release_date": "Wed, 28 Dec 1994 00:00:00 GMT",
                "title": "Shawshank Redemption"
            }
        ],
        "success": true
    }

GET '/actors'
- Fetches a list of actors form the database
- Request Arguments: None
- Returns:
    - actors_list - A list of actor objects

- Sample Output

    {
    "actors_list": [
        {
            "age": 67,
            "gender": "Male",
            "id": 1,
            "name": "Kamalhasan"
        }
    ],
    "success": true
    }

POST '/movies'
- Posts a new movie to the database
- Request Arguments: None
- Request Body : contains the title and release_date.

- Sample Body  

    {
    "title":"Shawshank Redemption",
    "release_date": "1994-12-28"
    }

Please not that the release_date should be in "yyyy-mm-dd" format

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

POST '/actors'
- Posts a new actor to the database
- Request Arguments: None
- Request Body : contains the name, age and gender.

- Sample Body  

    {
    "name":"Vijay",
    "age":46,
    "gender":"Male"
    }

Please not that the release_date should be in "yyyy-mm-dd" format

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

DELETE '/movies/<movie_id>'
- It deletes the movie with the passed movie_id
- Request Arguments: None
- Returns: Success as true if the movie_id was present , 404 error if the movie_id was not present

IF movie_id is available

{
  "success": true
}

IF movie_id is not available

{
  "error": 404,
  "message": "Not Found",
  "success": false
}

DELETE '/actors/<actor_id>'
- It deletes the actors with the passed mactor_idovie_id
- Request Arguments: None
- Returns: Success as true if the actor_id was present , 404 error if the actor_id was not present

IF actor_id is available

{
  "success": true
}

IF movie_id is not available

{
  "error": 404,
  "message": "Not Found",
  "success": false
}

PATCH '/actors/<actor_id>'
- It updates the actors with the passed actor , with the values passed in the body
- Request Arguments: None
- Request Body : could contain any one or all of name, age and gender.

- Sample Body  

  {
    "gender":"Female"
  }

- Returns: Success as true and the actor object if the actor_id was present , 404 error if the actor_id was not present

IF actor_id is available

{
    "actor": {
        "age": 46,
        "gender": "Female",
        "id": 2,
        "name": "Vijay"
    },
    "success": true
}

IF actor_id is not available

{
  "error": 404,
  "message": "Not Found",
  "success": false
}

PATCH '/movies/<movie_id>'
- It updates the movie with the passed actor , with the values passed in the body
- Request Arguments: None
- Request Body : could contain any one or all of name, age and gender.

- Sample Body  

  {
    "release_date": "2002-10-02"
  }

- Returns: Success as true and the movie object if the movie_id was present , 404 error if the movie_id was not present

IF movie_id is available

{
    "movie": {
        "id": 1,
        "release_date": "Wed, 02 Oct 2002 00:00:00 GMT",
        "title": "Shawshank Redemption"
    },
    "success": true
}

IF movie_id is not available

{
  "error": 404,
  "message": "Not Found",
  "success": false
}


```

## Testing
To run the tests,

```bash
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone_test.psql
python test_app.py
```

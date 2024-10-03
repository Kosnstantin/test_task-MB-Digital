Configuration
=============
1. pip install django djangorestframework
2. python(3) manage.py runserver
3. You can use the Postman for testing. Choose the type of query you want, and then paste in the body json code
4. GET: 
    http://127.0.0.1:8000/api/people, http://127.0.0.1:8000/api/teams
5. POST:
    http://127.0.0.1:8000/api/teams/
    Query:
        {
            "name": "Team name"
        }

    http://127.0.0.1:8000/api/people/
    Query:
        {
            "first_name": "Name,
            "last_name": "Surname",
            "email": "email@example.com",
            "team": {id}
        }
6. PATCH:
    http://127.0.0.1:8000/api/teams/{id}/
    Query:
        {
            "name": "New team name"
        }

    http://127.0.0.1:8000/api/people/{id}/
    Query:
        {
            "first_name": "New same,
            "last_name": "New surname",
            "email": "newemail@example.com",
            "team": 1 
        }
7. DELETE:
    http://127.0.0.1:8000/api/teams/{id}/
    http://127.0.0.1:8000/api/people/{id}/

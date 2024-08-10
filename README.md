Task Management System API

Table of Contents
1. Project Overview
2. Setup Instructions
3. Design Decisions
4. Running the Application
5. API Documentation
6. Request/Response Examples
7. Additional Documentation

1. Project Overview:-
The Task Management System API is a RESTful service that allows users to manage tasks. Users can create, read, update, and delete tasks with properties like title, description, status, priority, and due date. This system is designed to be easily extendable for future features like user authentication and task assignment.

2. Setup Instructions:- 

Prerequisites
Python 3.x
Django 4.x
Django REST Framework

Installation
Clone the repository:
git clone https://github.com/Prashant-Mamdyal/TMS_v1.git

Create and activate a virtual environment:
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

Access the API:
Open your browser or API client (e.g., Postman) and navigate to:
http://127.0.0.1:8000/api/tasks/

3. Design Decisions:-

Model Design-
The Task model was designed with fields such as title, description, status, priority, due_date, created_at, and updated_at to capture essential task details.
status and priority fields use choice fields to ensure data integrity and consistency.

Use of Django REST Framework-
DRF was chosen to leverage its powerful tools for building web APIs, including ModelViewSet and serializers.

RESTful API-
The API adheres to RESTful principles, ensuring predictable and standard behavior across endpoints.

4. Running the Application:-
To run the application, ensure you have followed the setup instructions. The application runs on the default Django development server.

Start the server-
python manage.py runserver

Access the API-
Visit http://127.0.0.1:8000/api/tasks/ in your browser


5. API Documentation:-
Endpoints-
Method	            Endpoint	            Description
GET	            /api/tasks/	            Retrieve a list of all tasks
GET	            /api/tasks/<id>/	    Retrieve a specific task by its ID
POST	        /api/tasks/	            Create a new task
PUT	            /api/tasks/<id>/	    Update an existing task
DELETE	        /api/tasks/<id>/	    Delete a specific task

6. Request/Response Examples:-
Create a Task:

Request:
POST- /api/tasks/
{
    "title": "Fix bug in module X",
    "description": "Fix the bug related to user authentication.",
    "status": "in_progress",
    "priority": "high",
    "due_date": "2024-10-08"
}

Response:
{
    "id": 1,
    "title": "Fix bug in module X",
    "description": "Fix the bug related to user authentication.",
    "status": "in_progress",
    "priority": "high",
    "due_date": "2024-10-08",
    "created_at": "2024-08-10T10:00:00Z",
    "updated_at": "2024-08-10T10:00:00Z"
}

7. Additional Documentation:-
Testing:
The application includes unit tests located in tasks/tests.py. Run tests using:

python manage.py test task
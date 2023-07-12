# Scribe

Scribe is a Django-based RESTful API application for managing a blog.

## Features

- Create, retrieve, update, and delete posts
- Assign categories and users to posts
- Filter and search posts by title, description, and category
- Pagination support for listing posts

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework 3.x

## Installation

1. Clone the repository:
```bash
$ git clone https://github.com/diina-gh/django-api.git
```

2. Create a virtual environment:

```bash
$ python3 -m venv env
```

3. Activate the virtual environment:
```bash
$ source env/bin/activate
```

4. Install the required dependencies:
```bash
$ pip install -r requirements.txt
```

5. Apply the database migrations:
```bash
$ python manage.py migrate
```

6. Start the development server:
```python
$ python manage.py runserver
```
  
7. Access the API at `http://localhost:8000/api/`

## Configuration

The main configuration files are:

- `settings.py`: Contains the Django project settings
- `urls.py`: Defines the API endpoint URLs and their associated views





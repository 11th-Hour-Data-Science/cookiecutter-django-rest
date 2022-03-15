# {{cookiecutter.project_name}}

[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}})
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

{{cookiecutter.description}}. Check out the project's [documentation](http://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repository_name}}/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

# Initialize the project

Start the dev server for local development in the API directory:

```bash
docker-compose up
```
The API should be available at http://localhost:8000/api/v1/ and the docs
should be available at http://localhost:8001

## Useful Commands

Initialize the database with migrations:
```bash
docker-compose run --rm api python manage.py makemigrations <app name>
docker-compose run --rm api python manage.py migrate
```

Seed the database with data:
```bash
docker-compose run --rm api python manage.py seed <number of stations>
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm api ./manage.py createsuperuser
```

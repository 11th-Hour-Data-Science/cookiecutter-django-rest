# {{cookiecutter.github_repository_name}}

[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}})
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

{{cookiecutter.description}}. Check out the project's [documentation](http://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repository_name}}/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```
When you first start or make changes to a model, you must run:
```bash
docker-compose run --rm api python manage.py makemigrations <app-name>
docker-compose run --rm api python manage.py migrate
```
To seed the database, run:
```bash
docker-compose run --rm api python manage.py seed <stations to create>
```

Run a command inside the docker container:

```bash
docker-compose run --rm api [command]
```

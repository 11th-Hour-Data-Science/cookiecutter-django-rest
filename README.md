<p align="center">
  <img width="64" src="media/cdr-icon.png" alt="cookiecutter-django-rest">
  <h3 align="center">cookiecutter-django-rest</h3>
  <p align="center">a factory for building bleeding edge, best practiced, scalable, rest apis</p>
  <p align="center">
    <a href="https://github.com/agconti/cookiecutter-django-rest/actions/workflows/push.yaml">
      <img src="https://github.com/agconti/cookiecutter-django-rest/actions/workflows/push.yaml/badge.svg?branch=master" alt="Build Status">
    </a>
    <a href="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/">
      <img src="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/shield.svg" alt="Dependencies">
    </a>
    <a href="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/">
      <img src="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/python-3-shield.svg" alt="Python 3">
    </a>
  </p>
</p>

## Data Science Clinic Django Rest Cookiecutter

Forked from [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest) and modified to suit specific needs of data science clinic and follow recommendatations of *Two Scoops of Django*

You need to make a scalable api on a deadline. You deeply care about the quality of your work.
`cookiecutter-django-rest` takes care of the details so you can focus on making your api awesome.  Scaffolding a project takes seconds and it gives you [authentication](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/docs/api/authentication.md), [user accounts](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/users/views.py), and the [docs](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/docs/api/users.md) and [tests](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/users/test/test_views.py) to support them. Just add your own resources to the api and start shipping. ✨ 💅



## Highlights
- Modern Python development with Python 3.8+
- Bleeding edge Django 3.0+
- Fully dockerized, local development via docker-compose.
- PostgreSQL 11.6+
- Start off with full test coverage and [continuous integration](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/.travis.yml).
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Always current dependencies and security updates enforced by [pyup.io](https://pyup.io/).
- A slim but robust foundation -- just enough to maximize your productivity, nothing more.

## Quick Start

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

```bash
brew install cookiecutter
```

Scaffold your project:
```
cookiecutter gh:11th-Hour-Data-Science/cookiecutter-django-rest
```

![Scaffolding](media/scaffolding.gif)

Example of the result: https://github.com/agconti/piedpiper-web

### Users

If cookiecutter.include_users == "yes", Try creating a user!

```bash
curl -d '{"username":"'"$RANDOM"'", "password":"test", "email":"test@test.com", "first_name":"test", "last_name":"user"}' \
     -H "Content-Type: application/json" \
     -X POST http:localhost:8000/api/v1/users/
```

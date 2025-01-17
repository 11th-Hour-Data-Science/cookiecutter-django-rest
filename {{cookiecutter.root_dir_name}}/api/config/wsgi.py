"""
WSGI config for {{ cookiecutter.project_name }} project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "ProductionConfig")

from configurations.wsgi import get_wsgi_application  # noqa
application = get_wsgi_application()

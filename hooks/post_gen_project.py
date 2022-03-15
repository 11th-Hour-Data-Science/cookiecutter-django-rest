import shutil
import os

include_users = "{{ cookiecutter.include_users }}"

if include_users != "yes":
    shutil.rmtree("api/apps/users")
    os.remove("api/docs/api/measurements.md")
    os.remove("api/docs/api/authentication.md")
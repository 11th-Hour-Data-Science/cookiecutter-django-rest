import shutil
import os

include_users = "{{ cookiecutter.include_users }}"

if include_users != "yes":
    shutil.rmtree("apps/users")
    os.remove("docs/api/measurements.md")
    os.remove("docs/api/authentication.md")
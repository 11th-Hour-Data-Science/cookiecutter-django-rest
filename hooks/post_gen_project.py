import shutil

include_users = "{{ cookiecutter.include_users }}"

if include_users != "yes":
    shutil.rmtree("apps/users")
========================
feincms3 example project
========================

Clone this repository::

    git clone https://github.com/matthiask/feincms3-example/
    cd feincms3-example

Setup a virtualenv (Python 3 is recommended for new projects, but you
can also use Python 2.7)::

    virtualenv -p python3 venv
    venv/bin/pip install -r requirements.txt

Run migrations and create a superuser::

    venv/bin/python manage.py migrate
    venv/bin/python manage.py createsuperuser

Import the fixtures::

    venv/bin/python manage.py loaddata fixtures/pages.json
    venv/bin/python manage.py loaddata fixtures/articles.json

Start the runserver::

    venv/bin/python manage.py runserver

Open ``http://127.0.0.1:8000/`` and ``http://127.0.0.1:8000/admin/`` and
dive in!

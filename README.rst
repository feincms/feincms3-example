========================
feincms3 example project
========================

Clone this repository::

    git clone https://github.com/matthiask/feincms3-example/
    cd feincms3-example

Setup a virtualenv::

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Run migrations and create a superuser::

    ./manage.py migrate
    ./manage.py createsuperuser

Import the fixtures::

    ./manage.py loaddata fixtures/pages.json
    ./manage.py loaddata fixtures/articles.json

Start the runserver::

    ./manage.py runserver

Open ``http://127.0.0.1:8000/`` and ``http://127.0.0.1:8000/admin/`` and
dive in!

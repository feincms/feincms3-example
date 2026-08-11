# AGENTS.md

## What this is

A minimal but complete feincms3 example project (pages CMS + an articles app
mounted through feincms3's applications support). It exists to be read and run,
not to be deployed — keep it small and obvious.

## Linting

Run all hooks over the whole tree:

```
prek -a
```

Hooks fix most things themselves; stage the result and run again. Ruff is
configured in `pyproject.toml` (`RUF012` and `E501` are ignored on purpose).

## Running the project

There is no test suite. Verify changes by running the app:

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata fixtures/pages.json fixtures/articles.json
./manage.py createsuperuser
./manage.py runserver
```

`./manage.py check` should only ever report the two `feincms3.W007` CKEditor 4
warnings; those come from feincms3's own rich text plugin.

## Migrations

Model definitions drift as the feincms3 / django-content-editor /
django-imagefield dependencies evolve. Add new migrations on top rather than
regenerating the initial ones, and keep `./manage.py makemigrations --check
--dry-run` clean.

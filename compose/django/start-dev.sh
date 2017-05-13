#!/bin/sh

# Run migrations
python manage.py migrate

# Load fixtures
python manage.py loaddata backend/users/fixtures.yaml
python manage.py loaddata backend/core/fixtures.yaml

# Start dev server
python manage.py runserver_plus 0.0.0.0:8000

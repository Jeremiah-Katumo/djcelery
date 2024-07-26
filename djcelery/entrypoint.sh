#!/bin/bash

echo "Database apply migrations"
python manage.py migrate

exec "$@"
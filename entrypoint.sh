#!/bin/bash

echo "running"

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"

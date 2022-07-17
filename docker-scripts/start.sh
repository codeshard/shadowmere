#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py collectstatic --no-input
gunicorn shadowmere.wsgi:application --bind 0.0.0.0:8001 -k gevent -w 6

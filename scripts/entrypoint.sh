#!/bin/bash

set -e

#newrelic-admin run-program gunicorn wsgi:app
uwsgi --http :${PORT} --module wsgi:app --master --processes 4 --threads 2

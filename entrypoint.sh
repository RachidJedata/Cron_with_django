#!/bin/sh

# Make and apply migrations using python3
python3 manage.py makemigrations
python3 manage.py migrate

# Prepare the cron log file
mkdir -p /cron
touch /cron/cron.log
chmod 666 /cron/cron.log

# Add the cron jobs from your settings.py
python3 manage.py crontab add

# Start the cron service in the background
service cron start &

# Run your Django server in the foreground to keep the container alive.
exec python3 manage.py runserver 0.0.0.0:8000
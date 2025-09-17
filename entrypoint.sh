#!/bin/sh


# Make and apply migrations
python3 manage.py makemigrations
python3 manage.py migrate


# Prepare the cron log file
mkdir -p /app/cron
touch /app/cron/cron.log
chmod 666 /app/cron/cron.log

# Add the cron jobs
python3 manage.py crontab add

# Start the cron in the background
service cron start

# Run your Django server in the foreground
# This command keeps the container alive
exec python3 manage.py runserver 0.0.0.0:8000
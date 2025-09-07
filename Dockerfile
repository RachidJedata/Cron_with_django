FROM python:3.10-slim

RUN apt-get update && apt-get install -y cron procps


RUN alias python=python3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
FROM python:slim

ENV SLEEP_TIME "6h"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["bash", "daemon.sh"]
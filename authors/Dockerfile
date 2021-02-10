FROM python:3.8-slim-buster

ADD app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD ./* /app/

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

STOPSIGNAL SIGTERM

ENTRYPOINT [ "gunicorn", "--log-level", "debug", "--graceful-timeout", "30", "--bind", "0.0.0.0:5000", "app:app" ]

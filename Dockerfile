FROM python:3.8-slim-buster

ADD src/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD ./* /app/

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

CMD [ "flask", "run", "--host=0.0.0.0" ]

FROM python:3.8-slim-buster

ADD src/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD ./* /app/

EXPOSE 5000

# python3 command runs db.create_all()
CMD ["python3", "app.py", "&&", "gunicorn", "--log-level", "debug", "--bind", "0.0.0.0:5000", "app:app" ]

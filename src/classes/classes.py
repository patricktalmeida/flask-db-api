import os
import mysql.connector
import logging
import sys
sys.path.append("..")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError, pre_load
# from main import app, db

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db

##### MODELS #####
class CreateDB:
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    
    def mysql_connect():
        connection = mysql.connector.connect(host=CreateDB.db_host,
                                            user=CreateDB.db_user,
                                            password=CreateDB.db_pass)

        return connection

    def create_db():
        connection = CreateDB.mysql_connect()

        db_creation = "CREATE DATABASE author;"

        try:
            with connection.cursor() as cursor:
                cursor.execute(db_creation)
                logging.info('Migrations completed!')
        except:
            logging.info('Database already exists!')
        finally:
            connection.close()

class Author(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))

class Quote(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("quotes", lazy="dynamic"))
    posted_at = db.Column(db.DateTime)


##### SCHEMAS #####
class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    first = fields.Str()
    last = fields.Str()
    formatted_name = fields.Method("format_name", dump_only=True)

    def format_name(self, author):
        return "{}, {}".format(author.last, author.first)

# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")


class QuoteSchema(Schema):
    id = fields.Int(dump_only=True)
    author = fields.Nested(AuthorSchema, validate=must_not_be_blank)
    content = fields.Str(required=True, validate=must_not_be_blank)
    posted_at = fields.DateTime(dump_only=True)

    # Allow client to pass author's full name in request body
    # e.g. {"author": "Tim Peters"} rather than {"first": "Tim", "last": "Peters"}
    @pre_load
    def process_author(self, data, **kwargs):
        author_name = data.get("author")
        if author_name:
            first, last = author_name.split(" ")
            author_dict = dict(first=first, last=last)
        else:
            author_dict = {}
        data["author"] = author_dict

        return data

import datetime

from flask import request
from sqlalchemy.exc import IntegrityError
from flask import Blueprint
from marshmallow import ValidationError
from app.classes.exeptions import DBDownException
from app.schemas.schemas import AuthorSchema, QuoteSchema
from app.models.models import Author, Quote, db

blue_print = Blueprint('app', __name__)
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True, only=("id", "content"))

@blue_print.route("/healthcheck")
def healthcheck():
    is_db_up = True

    try:
        db.session.execute('SELECT 1')
    except:
        is_db_up = False
        raise DBDownException
    return 'API is ready to recieve connections!', 200

@blue_print.route("/authors")
def get_authors():
    authors = Author.query.all()
    # Serialize the queryset
    result = authors_schema.dump(authors)

    return {"authors": result}

@blue_print.route("/authors/<int:pk>")
def get_author(pk):
    try:
        author = Author.query.get(pk)
    except IntegrityError:
        return {"message": "Author could not be found."}, 400
    
    author_result = author_schema.dump(author)
    quotes_result = quotes_schema.dump(author.quotes.all())

    return {"author": author_result, "quotes": quotes_result}

@blue_print.route("/quotes/", methods=["GET"])
def get_quotes():
    quotes = Quote.query.all()
    result = quotes_schema.dump(quotes, many=True)

    return {"quotes": result}

@blue_print.route("/quotes/<int:pk>")
def get_quote(pk):
    try:
        quote = Quote.query.get(pk)
    except IntegrityError:
        return {"message": "Quote could not be found."}, 400
    
    result = quote_schema.dump(quote)

    return {"quote": result}

@blue_print.route("/quotes/", methods=["POST"])
def new_quote():
    json_data = request.get_json()
    
    if not json_data:
        return {"message": "No input data provided"}, 400

    # Validate and deserialize input    
    try:
        data = quote_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    
    first, last = data["author"]["first"], data["author"]["last"]
    author = Author.query.filter_by(first=first, last=last).first()
    
    if author is None:
        # Create a new author
        author = Author(first=first, last=last)
        db.session.add(author)
    # Create new quote
    quote = Quote(
        content=data["content"], author=author, posted_at=datetime.datetime.utcnow()
    )
    db.session.add(quote)
    db.session.commit()
    result = quote_schema.dump(Quote.query.get(quote.id))

    return {"message": "Created new quote.", "quote": result}, 201

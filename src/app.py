import time

from classes import db, app, CreateDB
from routes import *

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True, port=5000, host='0.0.0.0')

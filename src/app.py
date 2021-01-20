import time

from classes import db, app, CreateDB
from routes import *

if __name__ == "__main__":
    # wait for mysql
    time.sleep(5)
    CreateDB.create_db()
    db.create_all()

    # Finish python process to serve with gunicorn
    import psutil
    PROCNAME = "app.py"
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()    

    app.run(debug=True, port=5000, host='0.0.0.0')

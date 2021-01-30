class DBDownException(Exception):
    def __init__(self, message='Check if DB is up'):
        self.message = message

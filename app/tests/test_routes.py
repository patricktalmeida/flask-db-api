import unittest
import sys
sys.path.append("..")

from mock.mock_test_routes import TestRoutesMock
from app.routes import get_authors, get_author, get_quote, get_quotes

class TestRoutes(unittest.TestCase):
    """
    Unitest for Routes methods
    """
    def test_get_authors(self):
        author = TestRoutesMock.get_authors_mock()

        self.assertTrue(str(author["author"]["first"]))
        self.assertTrue(str(author["author"]["formatted_name"]))
        self.assertTrue(str(author["author"]["id"]))
        self.assertTrue(str(author["author"]["last"]))

if __name__ == '__main__':
    unittest.main()

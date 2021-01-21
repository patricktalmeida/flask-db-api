class TestRoutesMock:
    def get_authors_mock():
        example_author = {
            "author": {
                "first": "John", 
                "formatted_name": "Doe, John", 
                "id": 1, 
                "last": "Doe"
            }, 
            "quotes": [
                {
                "content": "Poetry is awsome.", 
                "id": 1
                }, 
                {
                "content": "Poetry is pretty awsome.", 
                "id": 2
                }, 
                {
                "content": "Poetry is awsome.", 
                "id": 5
                }, 
                {
                "content": "Poetry is pretty awsome.", 
                "id": 6
                }
            ]
        }
        return example_author

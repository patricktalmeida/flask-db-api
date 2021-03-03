from locust import HttpUser, TaskSet, task, tag
import logging
import os

class Cls:
    counter = 0
    def __init__(self):
        Cls.counter += 1

    def count(self):
        return Cls.counter

    def __repr__(self):
        return f'{Cls.counter}'

@tag('graceful-shutdown')
class Write(TaskSet):
    client_token = os.getenv('CLIENT_TOKEN')

    @task()
    def write(self):
        payload = {
            "author":"John Doe",
            "content":f"Post number {Cls()}"
        }

        with self.client.post('/api/quotes', 
                            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.client_token}"},
                            json=payload, 
                            name='Quote Registration', 
                            catch_response=True
                        ) as response:
            logging.info(response.request.body)
            if (response.status_code == 201):
                logging.info('Quote successfully registered.')
            else:
                logging.error(str(response.status_code) +
                              ' -- ' + response.text)

class UserSigningUp(HttpUser):
    tasks = [Write]

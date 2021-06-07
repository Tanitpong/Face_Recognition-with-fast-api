from locust import HttpUser, task, between
import json
import requests

class QuickstartUser(HttpUser):
    min_wait = 1000
    max_wait = 2000

    @task
    def test_api(self):
        self.client.get("/users")
        url = "127.0.0.1:8000/img"
        payload={}
        files=[
            ('file',('301684.jpg',open('Testload_api/301685.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
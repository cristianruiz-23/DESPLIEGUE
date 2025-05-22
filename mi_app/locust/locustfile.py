from locust import HttpUser, task, between
import random
import string

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def get_items(self):
        self.client.get("/items")

    @task(2)
    def create_item(self):
        random_name = ''.join(random.choices(string.ascii_letters, k=8))
        self.client.post(f"/items?name={random_name}")

from locust import HttpUser, task

class MyWebsiteUser(HttpUser):
    @task
    def load_test(self):
        self.client.get("/")

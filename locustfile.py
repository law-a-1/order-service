from locust import HttpUser, task

class ApplicationOrder(HttpUser):

    @task
    def index(self):
        logging = {
            "type": "ERROR",
            "service" : "order",
            "message": "404 - Order not found"
        }
        self.client.post('/logs',json=logging)
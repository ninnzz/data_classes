from locust import HttpUser, task


class DataClassExperimentUser(HttpUser):

    @task
    def rjson(self):
        self.client.get("/get_rider/json")

    @task
    def rdataclass(self):
        self.client.get("/get_rider/dataclass")

    @task
    def rbasemodel(self):
        self.client.get("/get_rider/basemodel")

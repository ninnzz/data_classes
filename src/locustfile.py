from locust import HttpUser, task, tag


class DataClassExperimentUser(HttpUser):

    @tag("json")
    @task
    def rjson(self):
        self.client.get("/get_rider/json")

    @tag("jsonval")
    @task
    def rjson(self):
        self.client.get("/get_rider/jsonvalidation")

    @tag("dataclass")
    @task
    def rdataclass(self):
        self.client.get("/get_rider/dataclass")

    @tag("basemodel")
    @task
    def rbasemodel(self):
        self.client.get("/get_rider/basemodel")

# data_classes
Dataclass experiments

# TODO

- [ ] Create an outline
- [ ] Dataclass speed on apis, with data class vs raw json
- [x] Dataclass speed on apis with checks (use fastapi)
- [ ] Dataclass on datascience and ML projects, check speed and benchmark


### API load testing

Test if using dataclass or BaseModel of pydantic affects the response time of an api.

- Load testing using [locust](https://docs.locust.io/en/stable/quickstart.html)
- API built using fast api 
- Create 4 apis to compare
  - `GET /get_rider/json` plain json response
  - `GET /get_rider/jsonvalidation` plain json response with some data validation
  - `GET /get_rider/dataclass` return as `pydantic.dataclass`
  - `GET /get_rider/basemodel` return as `pydantic.BaseModel` using a response model

Run the api:

```shell
poetry run uvicorn src.server:app --reload
```

Run locust testing

```shell
poetry run locust -f src/locustfile.py
# open http://0.0.0.0:8089 to run load test
```

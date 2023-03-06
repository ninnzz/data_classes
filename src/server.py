from fastapi import FastAPI
# Enhanced dataclass.dataclass object
from pydantic.dataclasses import dataclass
app = FastAPI()


@dataclass
class Rider:
    name: str = ""
    age: int = 0
    weight: int = 0
    height: int = 0


@dataclass
class Suspension:
    brand: str = ""
    travel: int = 0
    model: str = ""

@dataclass
class Bike:
    frame_brand: str = ""
    model: str = ""
    rear_suspension: Suspension = None
    front_suspension: Suspension = None


@dataclass
class GetRiderResponse:
    rider: Rider
    bike: Bike


def generate_data() -> dict:
    """
    Simulate generate data somewhere.

    :return:
    :rtype:
    """

    return {
        "rider": {
            "name": "rider1",
            "age": 25,
            "weight": 75,
            "height": 170
        },
        "bike": {
            "frame_brand": "canyon",
            "model": "spectral",
            "rear_suspension": {
                "brand": "rockshox",
                "travel": 150,
                "model": "deluxe select +"
            },
            "front_suspension": {
                "brand": "rockshox",
                "travel": 150,
                "model": "pike select"
            }
        }

    }


@app.get("/get_rider/json")
async def get_rider_json():
    """
    Json api call.

    :return:
    :rtype:
    """

    rider_profile = generate_data()

    return rider_profile


@app.get("get_rider/dataclass")
async def get_rider_dataclass():
    """
    Dataclass api call.

    :return:
    :rtype:
    """

    return {}

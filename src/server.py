from fastapi import FastAPI
# Enhanced dataclass.dataclass object
from pydantic.dataclasses import dataclass
from pydantic import BaseModel

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


class GetRiderResponseBaseModel(BaseModel):
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
            "age": "12",
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


@app.get("/get_rider/jsonvalidation")
async def get_rider_json_with_validation():
    """
    Json api call with validation.

    :return:
    :rtype:
    """

    rider_profile = generate_data()

    check_cols = ["age", "weight", "height"]
    # Add simple validation and serialization
    for col in check_cols:
        if not rider_profile["rider"][col].isnumeric():
            raise ValueError(f"'{col}' is not a number")
        else:
            rider_profile["rider"][col] = int(rider_profile["rider"][col])

    return rider_profile


@app.get("/get_rider/dataclass", response_model=GetRiderResponse)
async def get_rider_dataclass() -> GetRiderResponse:
    """
    Dataclass api call.

    :return:
    :rtype:
    """

    rider_profile = generate_data()

    resp = GetRiderResponse(
        rider=Rider(**rider_profile["rider"]),
        bike=Bike(
            frame_brand=rider_profile["bike"]["frame_brand"],
            model=rider_profile["bike"]["model"],
            rear_suspension=Suspension(**rider_profile["bike"]["rear_suspension"]),
            front_suspension=Suspension(**rider_profile["bike"]["front_suspension"])
        )
    )

    return resp


@app.get("/get_rider/basemodel", response_model=GetRiderResponseBaseModel)
async def get_rider_basemodel():
    """
    BaseModel api call.

    :return:
    :rtype:
    """

    rider_profile = generate_data()

    return rider_profile

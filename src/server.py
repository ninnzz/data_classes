from fastapi import FastAPI

app = FastAPI()


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
    

@app.get("/")
async def root():
    return {"message": "Hello World"}
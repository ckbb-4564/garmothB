from fastapi import FastAPI

app = FastAPI()

grindspots = {
    1: {
        "name": "Thornwood Forest",
        "type": "Kamasylvia"
    },
    2: {
        "name": "Tunkuta",
        "type": "Kamasylvia"
    },
    3: {
        "name": "Olun Valley",
        "type": "Kamasylvia"
    },
    4: {
        "name": "Crypt of Resting's Thought",
        "type": "Kamasylvia"
    }
}

@app.get("/")
def home():
    return {"message": "home"}

@app.get("/grindspots")
def get_grindspots():
    return grindspots

@app.get("/grindspot/{id}")
def get_grindspot(id: int):
    return grindspots[id]
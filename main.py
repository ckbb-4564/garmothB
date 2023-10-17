from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Grindspot(BaseModel):
    name: str
    type: str
    area: str

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

@app.get("/grindspot/")
def get_grindspot_by_name(name: str):
    for id in grindspots:
        if grindspots[id]["name"] == name:
            return grindspots[id]
    return "Error"

@app.post("/grindspot/create")
def create_grindspot(item: Grindspot):
    ids = grindspots.keys()
    id = list(ids)[-1] + 1
    grindspots[id] = {"name": item.name, "type": item.type}
    return item
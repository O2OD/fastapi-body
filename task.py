from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

items = []

@app.get("/items")
async def get_item():
    return items

@app.post("/items")
async def create_item(item:Item):
    items.append(item.model_dump())
    return {"status": "qo'shildi",
            "data": item
            }


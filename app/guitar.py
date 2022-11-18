from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field
from random import randint

app = FastAPI()

class Guitar(BaseModel):
    name: str = Field(max_length=100, title= "The name of the guitar")
    brand: str = Field(max_lengt= 50, title= "The name of the brand")
    price: float = Field(gt=0, title= "The price of the guitar")
    year: int | None = Field(default=None, title= "The year the guitar was made")


guitar_robbe = {
    "name": "Natura D550",
    "brand": "Walden",
    "price": 299,
    "year": 2015
}
guitar_julie = {
    "name": "example d22",
    "brand": "example",
    "price": 444,
    "year": 2202
}

guitars = {0: guitar_robbe, 1: guitar_julie}

@app.post("/guitars")
async def create_guitar(guitar: Guitar):
    new_key = len(guitars)
    guitars[new_key] = guitar
    return guitars[new_key]

@app.get("/guitars")
async def get_guitar(guitar_key: int | None = Query(default=None, ge=0, lt= len(guitars))):
    if guitar_key:
        return guitars[guitar_key]
    else:
        guitar_key = randint(0, len(guitars)-1)
        return guitars[guitar_key]

@app.put("/guitars/{guitar_key}")
async def get_guitar(*, guitar_key: int = Path(ge=0, lt= len(guitars)), guitar: Guitar):
    guitars[guitar_key] = guitar
    return guitars[guitar_key]
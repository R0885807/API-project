from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field, HttpUrl
from random import randint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com"
    "http://127.0.0.1:8000",
    "https://r0885807.github.io",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Guitar(BaseModel):
    name: str = Field(max_length=100, title= "The name of the guitar")
    brand: str = Field(max_lengt= 50, title= "The name of the brand")
    price: float = Field(gt=0, title= "The price of the guitar")
    year: int | None = Field(default=None, title= "The year the guitar was made")
    image: HttpUrl | None = Field(default=None, title= "Picture of the guitar")


guitar_robbe = {
    "name": "Natura D550",
    "brand": "Walden",
    "price": 190,
    "year": 2015,
    "image": "https://images.pexels.com/photos/10343848/pexels-photo-10343848.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
}
guitar_fender = {
    "name": "Player Stratocaster PF",
    "brand": "Fender",
    "price": 660,
    "year": 2016,
    "image": "https://d1aeri3ty3izns.cloudfront.net/media/36/369362/1200/preview.jpg"
}
guitar_Epiphone = {
    "name": "Les Paul Express",
    "brand": "Epiphone",
    "price": 151,
    "year": 2018,
    "image": "https://static.bax-shop.es/image/product/332311/959778/6dd1ce06/1488954820Epiphone_Les_Paul_Express_Ebony.jpg"
}
guitar_Gretsch = {
    "name": "G9126",
    "brand": "Gretsch",
    "price": 214,
    "year": 2017,
    "image": "https://cdn11.bigcommerce.com/s-8wy6p2/images/stencil/1000x1000/products/6354/129904/gretsch-g9126-guitar-ukulele-with-gig-bag-ovangkol-fingerboard-honey-mahogany-stain__01799.1645572384.jpg?c=2"
}
guitar_Ibanez = {
    "name": "RG5320",
    "brand": "Ibanez",
    "price": 2033,
    "year": 2022,
    "image": "https://d1aeri3ty3izns.cloudfront.net/media/57/577995/600/preview.jpg"
}
guitar_Yamaha = {
    "name": "F370",
    "brand": "Yamaha",
    "price": 192,
    "year": 2021,
    "image": "https://static.bax-shop.es/image/product/30280/146421/388cd49e/Yamaha-F370-Black_01.jpg"
}
guitar_martin = {
    "name": "000C12-16E",
    "brand": "Martin",
    "price": 2643,
    "year": 2021,
    "image": "https://www.martinguitar.com/dw/image/v2/BGJT_PRD/on/demandware.static/-/Sites-martin-master-catalog/default/dw72cf8ce7/images/000C12-16E-NYLON/000C12-16E-NYLON_f.jpg?sw=1600&sh=1600&sm=fit"
}
guitar_Ortega = {
    "name": "RUOCEAN Concert Acoustic",
    "brand": "Ortega",
    "price": 80,
    "year": 2022,
    "image": "https://d1aeri3ty3izns.cloudfront.net/media/67/677841/1200/preview.jpg"
}

guitars = {0: guitar_robbe, 1: guitar_fender, 2: guitar_Epiphone, 3: guitar_Gretsch, 4: guitar_Ibanez, 5: guitar_Yamaha, 6: guitar_martin, 7: guitar_Ortega}

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
async def get_guitar(*, guitar_key: int = Path(default=None, ge=0, lt= len(guitars)), guitar: Guitar):
    guitars[guitar_key] = guitar
    return guitars[guitar_key]

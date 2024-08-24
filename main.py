from fastapi import FastAPI, Path, Query
from enum import Enum

from fastapi.params import Query
from pydantic import BaseModel
import json
from typing import Annotated
from requests import JSONDecodeError
from fastapi.middleware.cors import CORSMiddleware


class User(BaseModel):
    name: str
    last_name: str
    password: str
    age: int

    # description: str | None = None
    # price: float
    # tax: float | None = None
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"hello": "hello"}


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = dict(item)
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

#
# @app.get("/items/")
# async def reat_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# dog_data = {
# "name": "Frieda",
#   "is_dog": True,
#   "hobbies": ["eating", "sleeping", "barking",],
#   "age": 8,
#   "address": {
#     "work": None,
#     "home": ("Berlin", "Germany",),
#   },
#   "friends": [
#     {
#       "name": "Philipp",
#       "hobbies": ["eating", "sleeping", "reading",],
#     },
#     {
#       "name": "Mitch",
#       "hobbies": ["running", "snacking",],
#     },
#   ],
# }
#
#
# with open("data.json", "w", encoding="utf-8") as write_file:
#     data = json.dump(dog_data, write_file, indent=4)
#     print(data)
#     write_file.close()
#
# with open("data.json", "r", encoding="utf-8") as read_file:
#     data = json.loads(read_file.read())
#     print(data)

#
# with open("data.json", mode="w", encoding='utf-8') as write_file:
#     json.dump(dog_data, write_file, indent=None, separators=(",", ":"))
#     write_file.close()
#
# with open("data.json", mode='r', encoding='utf-8') as read_file:
#     data = json.loads(read_file.read())
#     print(data)

# dog_registry = {1: {"name": "Ferieda"}}
# dog_json = json.dumps(dog_registry)
# print(dog_json)
#
# load_back = json.loads(dog_json)
# print(load_back)
#
# print(load_back == dog_json)

# food_ratings = {"organic dog food": True, "human food": False}
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
# print(str(food_ratings))
# print(json.dumps(food_ratings))

# toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
# print(json.dumps(toy_conditions, sort_keys=True, indent=True))

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "user_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description."})
#     return item

# @app.get("/items/")
# async def read_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# class ModelName(str, Enum):
#     alexnet = 'alexnet'
#     resnet = 'resnet'
#     lenet = 'lenet'
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name}
#     if model_name.value == ModelName.resnet:
#         return {"model_name": model_name}
#     else:
#         return {"model_name": model_name}


# @app.get("/")
# def home():
#     return {"Hello": "World"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}
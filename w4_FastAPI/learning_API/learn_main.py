# from typing import Union
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root(): # 或是用index(): 這也可以
#     return {"Hello": "World"}
# # http://127.0.0.1:8000/
# # http://127.0.0.1:8000
# # 這個是得出"Hello": "World"


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
# # http://127.0.0.1:8000/items/5?q=some
# # 網址的"5" 可以改成其他數字，"item_id"的值也會相對應修改
# # q=some，這也可以改成其他，"q"也會修改
# # "item_id": 80,
# # "q": "some"



# # uvicorn learn_main:app --reload



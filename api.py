# from fastapi import FastAPI, HTTPException, Header, Response, File, UploadFile, Depends
# import io
# from fastapi.responses import FileResponse
# from pydantic import BaseModel
# from fastapi.params import Query
# from typing import Optional
# import time
# from enum import Enum
# from fastapi.security import OAuth2PasswordBearer

# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine
# # ORM - sqlalchemy
# # nếu chưa có thì sẽ tạo cơ sơ dữ liệu sqlite
# # echo: nhật ký hoạt động
# engine = create_engine('sqlite:///sales.db', echo = True)


# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# # Định nghĩa một lớp người dùng
# # phải có __tablename__ và ít nhất 1 column là một phần của khoá chính
# # lớp người dùng này có thể thiếu hoặc dư field so với db
# # nếu thiếu field so với db: thì kệ, vì code làm việc với class User được định nghĩa bên dưới(coi như db dư field)
# # nếu class nhiều field hơn db: thì sẽ được update vào db
# class Users(Base):
#     __tablename__ = "Users"
#     id = Column(Integer, primary_key = True)
#     name = Column(String)
#     address = Column(String)
#     email = Column(String)
# # đối với các bảng chưa tạo nó sẽ create
# Base.metadata.create_all(engine)
# # sqlite
# # CREATE TABLE "Users" (
# #     id INTEGER NOT NULL, 
# #     name VARCHAR, 
# #     address VARCHAR, 
# #     email VARCHAR, 
# #     PRIMARY KEY (id)
# # )




# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}

# @app.get("/")
# async def read(item: int, it: int):
#     if item != 11:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
#         )
#     return {"Hello" : "World" + str(item)}
#     # return FileResponse('/Users/trinhtran/Desktop/a.jpg');

# @app.get("/{id}", status_code=201)
# async def read(id:Optional[int] = 1):
#     return {"Hello" : "World" + str(id)}

# @app.get("/{name}")
# async def read(name: ModelName):
    
#     return {"Hello" : "World"}

# @app.get("/headers-and-object/")
# def get_headers(response: Response):
#     response.headers["X-Cat-Dog"] = "alone in the world"
#     return {"message": "Hello World"}

# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": file}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     contents = await file.read()
#     print(contents)
#     return {"filename": file}

# @app.get("/api")
# def read():
#     return FileResponse('/Users/trinhtran/Desktop/a.jpg');


from fastapi import FastAPI
import models, schemas
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

from routers import items
from routers.users import router as router_users
from internal import admin
import models, schemas
from database import engine

app = FastAPI(title="Trinh Tran")

models.Base.metadata.create_all(engine  )


# router default
@app.get("/")
def read():
    return {"hello": "world"}

# router riêng
app.include_router(items.router, tags=["items"], prefix="/task")
# router riêng
app.include_router(router_users, tags=["users"], prefix="/user")

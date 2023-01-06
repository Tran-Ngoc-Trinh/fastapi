from pydantic import BaseModel, Field

#  xác nhận dữ liệu hợp lệ

class User(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        schema_extra = {
            "example" : {
                "username": "Tran Ngoc Trinh",
                "email": "ngoctrinh2633@gmail.com",
                "password": "123456"
            }
        }

class Login(BaseModel):
    email: str
    password: str
    class Config:
        schema_extra = {
            "example" : {
                "email": "ngoctrinh2633@gmail.com",
                "password": "123456"
            }
        }
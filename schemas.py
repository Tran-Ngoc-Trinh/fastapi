from pydantic import BaseModel, Field

#  xác nhận dữ liệu hợp lệ

class User(BaseModel):
    name: str
    address: str
    email: str
    class Config:
        schema_extra = {
            "example" : {
                "name": "Tran Ngoc Trinh",
                "address": "103A Nguyen Thong",
                "email": "ngoctrinh2633@gmail.com"
            }
        }
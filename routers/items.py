from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User


router = APIRouter()
engine = create_engine('sqlite:///sales.db', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

@router.get("/", response_description="get list all tasks")
async def Get_items():
    
    Session = sessionmaker(bind = engine)
    session = Session()
    result = session.query(Users)
    return {"name": result[0].name}

@router.get("/{id}", response_description="get task detail")
async def Get_item(id: str):
    try:
        result = session.query(Users).filter(Users.id == id)
        return {"name": result[0].name}
    except:
        raise HTTPException(status_code=404, detail=f"task id = {id} not found")

@router.delete("/{id}", response_description="delete a task")
async def delete_item(id: str):
    json_compatible_item_data = jsonable_encoder({"hello": "world"})
    return JSONResponse(content=json_compatible_item_data,status_code=status.HTTP_204_NO_CONTENT)

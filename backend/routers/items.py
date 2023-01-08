from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List


import models as models, schemas as schemas
from database import SessionLocal, get_db
import crud as crud


router = APIRouter()


@router.get("/", response_description="get users", )
async def Get_users(skip:int = 0, limit: int=100,db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return users

@router.get("/{user_id}", response_description="get user")
async def Get_user(user_id:int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_description="add user", status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, request)
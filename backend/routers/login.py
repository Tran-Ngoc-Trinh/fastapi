from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List
from auth.jwt_bearer import jwtBearer
from auth.jwt_handler import signJWT,validate_token
import models as models, schemas as schemas
from database import SessionLocal, get_db
import crud as crud


router = APIRouter()


@router.post("/signup", response_description="signup", status_code=status.HTTP_201_CREATED )
async def Signup(request: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=signJWT(request.email)['access token'])
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    request.email = signJWT(request.email)['access token']
    crud.create_user(db, request)
    return {
        'access token': request.email
    }

@router.post("/login", response_description="log in", status_code=status.HTTP_200_OK )
async def Login(request: schemas.Login, db: Session = Depends(get_db)):
    db_user = crud.checkLogin(db, signJWT(request.email)['access token'],  request.password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        'access token': db_user.email
    }
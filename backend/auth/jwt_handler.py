import time
import jwt
from dotenv import dotenv_values
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import ValidationError
import crud as crud
from sqlalchemy.orm import sessionmaker, Session
from database import SessionLocal, get_db

config = dotenv_values("./.env")

JWT_SECRET = config['secret']
JSWT_ALGORITHM = config['algorithm']
reusable_oauth2 = HTTPBearer(scheme_name='Authorization')



def token_response(token: str):
    return {
        "access token": token
    }

def signJWT(userID: str):
    payload = {
        "userID": userID
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JSWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JSWT_ALGORITHM])
        return decode_token
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Not enough segments",
            headers={"WWW-Authenticate": "Bearer error='Not enough segments'"},
        )

def validate_token(beerer=Depends(reusable_oauth2), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=beerer.credentials)
    if(db_user is None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer error='invalid_token'"},
        )
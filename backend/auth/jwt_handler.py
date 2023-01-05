import time
import jwt
from dotenv import dotenv_values

config = dotenv_values("./.env")

JWT_SECRET = config.get('secret')
JSWT_ALGORITHM = config.get('algorithm')

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
    decode_token = jwt.decode(token, JWT_SECRET, algorithm=JSWT_ALGORITHM)
    return decode_token
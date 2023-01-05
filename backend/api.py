from fastapi import FastAPI,Request, status, Response , File, UploadFile, Form, Depends
import models
from sqlalchemy import create_engine

from routers import items
from routers.users import router as router_users
from internal import admin
from database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI(title="Trinh Tran")

app.mount("/static", StaticFiles(directory="backend/static", html=True), name="static")
templates = Jinja2Templates(directory="backend/templates/")

models.Base.metadata.create_all(engine)

class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request):
        return await super().dispatch(request)

# app.add_middleware(
#     # BaseHTTPMiddleware
#     # CORSMiddleware,
#     # allow_origins=["http://localhost:8080", "http://localhost:3000"],
#     # allow_credentials=True,
#     # allow_methods=["*"],
#     # allow_headers=["*"],
# )

# router default
# @app.get("/",response_class=HTMLResponse)
# def read(request: Request):
#     id = 3
#     return templates.TemplateResponse("index.html", {"request": request,"id": id})
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.post('/token')
async def token(formdata: OAuth2PasswordRequestForm = Depends()):
    return {'acc': formdata.username + 'token'}
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# router riêng
app.include_router(items.router, tags=["items"], prefix="/task")
# router riêng
app.include_router(router_users, tags=["users"], prefix="/user")

# api phụ
subapi = FastAPI()

@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}

app.mount("/subapi", subapi)

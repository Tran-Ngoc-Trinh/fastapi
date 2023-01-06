from fastapi import FastAPI,Request, status, Response , File, UploadFile, Form, Depends, HTTPException
import models
from sqlalchemy import create_engine
from schemas import Login
from routers import items, users, login
from routers.users import router as router_users
from internal import admin
from database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.jwt_handler import signJWT,validate_token
from fastapi.security import HTTPBearer
from auth.jwt_bearer import jwtBearer


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
@app.get("/",response_class=HTMLResponse)
def read(request: Request):
    id = 3
    return templates.TemplateResponse("index.html", {"request": request,"id": id})




# bearer
@app.get('/books', dependencies=[Depends(validate_token)])
def list_books():
    return {'data': ['Sherlock Homes', 'Harry Potter', 'Rich Dad Poor Dad']}

@app.post('/post', dependencies=[Depends(jwtBearer())])
def list_books():
    return {'data': ['Sherlock Homes', 'Harry Potter', 'Rich Dad Poor Dad']}                                                                                                                


# router riêng
app.include_router(login.router, tags=["Login"], prefix="/api/v1")
# router riêng
app.include_router(items.router, tags=["items"], prefix="/api/v1/task")
# router riêng
app.include_router(users.router, tags=["users"], prefix="/api/v1/user")

# api phụ
subapi = FastAPI()

@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}

app.mount("/subapi", subapi)

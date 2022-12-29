from fastapi import FastAPI
import models as models, schemas as schemas
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

from routers import items
from routers.users import router as router_users
from internal import admin
import models as models, schemas as schemas
from database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="Trinh Tran")

app.mount("/static", StaticFiles(directory="backend/static"), name="static")
# <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">
templates = Jinja2Templates(directory="backend/templates/")

models.Base.metadata.create_all(engine)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:8080"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# router default
@app.get("/",response_class=HTMLResponse)
def read():
    return templates.TemplateResponse("index.html", {"request": {}})


# router riêng
app.include_router(items.router, tags=["items"], prefix="/task")
# router riêng
app.include_router(router_users, tags=["users"], prefix="/user")

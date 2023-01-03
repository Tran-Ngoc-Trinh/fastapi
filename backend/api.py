from fastapi import FastAPI,Request
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
from starlette.middleware.base import BaseHTTPMiddleware

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
    # return "abcd"


# router riêng
app.include_router(items.router, tags=["items"], prefix="/task")
# router riêng
app.include_router(router_users, tags=["users"], prefix="/user")

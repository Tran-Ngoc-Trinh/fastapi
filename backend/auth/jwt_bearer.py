from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# @app.post("/post", dependencies=[Depends(jwtBearer())])
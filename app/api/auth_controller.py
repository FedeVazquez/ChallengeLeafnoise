from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.core.security import create_access_token
from app.core.config import ADMIN_USERNAME, ADMIN_PASSWORD

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest):
    """
    Autentica al usuario y genera un token JWT.
    """
    if credentials.username != ADMIN_USERNAME or credentials.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token({"sub": credentials.username})
    return {"access_token": access_token, "token_type": "bearer"}
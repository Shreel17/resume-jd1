from fastapi import APIRouter, HTTPException
from jose import jwt, JWTError

from models import RecruiterAuth, RefreshTokenRequest
from auth_service import signup_recruiter, login_recruiter, create_access_token
from config import JWT_SECRET, JWT_ALGORITHM
from pymongo.errors import DuplicateKeyError

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(data: RecruiterAuth):
    try:
        return signup_recruiter(data.email, data.password)

    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already registered")

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
def login(data: RecruiterAuth):
    tokens = login_recruiter(data.email, data.password)
    if not tokens:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return tokens

@router.post("/refresh")
def refresh_token(data: RefreshTokenRequest):
    try:
        payload = jwt.decode(
            data.refresh_token,
            JWT_SECRET, #type:ignore
            algorithms=[JWT_ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        return {
            "access_token": create_access_token(
                {"sub": payload["sub"]}
            )
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

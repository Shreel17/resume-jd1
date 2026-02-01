from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from config import JWT_SECRET, JWT_ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# def get_current_recruiter(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM]) #type:ignore
#         if payload.get("type") != "access":
#             raise HTTPException(status_code=401)
#         return payload["sub"]
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")


def get_current_recruiter(token: str = Depends(oauth2_scheme)) -> str:
    """
    Extract recruiter_id from JWT access token
    """
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,  # type: ignore
            algorithms=[JWT_ALGORITHM]
        )

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type"
            )

        recruiter_id = payload.get("sub")
        if not recruiter_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )

        return recruiter_id

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

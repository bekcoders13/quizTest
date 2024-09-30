from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm.session import Session
from db import database
from models.user import Users
from schemas.token import TokenData, Token
from schemas.user import CreateUser
from utils.hash_password import pwd_context

session = Session()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

login_router = APIRouter(tags=['Login and Refresh token'])


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=150)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session = Depends(database), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone_number: Optional[str] = payload.get("sub")
        if phone_number is None:
            raise credentials_exception
        token_data = TokenData(phone_number=phone_number)
    except JWTError:
        raise credentials_exception
    user = db.query(Users).where(Users.phone_number == token_data.phone_number).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: CreateUser = Depends(get_current_user)):
    return current_user


@login_router.post("/token")
async def login_for_access_token(db: Session = Depends(database), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(Users).filter(Users.phone_number == form_data.username).first()
    if user:
        is_validate_password = pwd_context.verify(form_data.password, user.password)
    else:
        is_validate_password = False

    if not is_validate_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login yoki parolda xatolik",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.phone_number}, expires_delta=access_token_expires
    )
    db.query(Users).filter(Users.id == user.id).update({
        Users.token: access_token
    })
    db.commit()
    return {'id': user.id, "access_token": access_token, "token_type": "bearer"}


def token_has_expired(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload.get("exp"))
        current_time = datetime.utcnow()
        return current_time > expiration_time
    except jwt.JWTError:
        return False


@login_router.post("/refresh_token", response_model=Token)
async def refresh_token(
    db: Session = Depends(database),
    token: str = None
):
    user = db.query(Users).where(Users.token == token).first()
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Token error",
        )

    if not token_has_expired(token):
        raise HTTPException(
            status_code=400,
            detail="Token has not expired",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.phone_number},
        expires_delta=access_token_expires
    )
    db.query(Users).filter(Users.id == user.id).update({
        Users.token: access_token
    })
    db.commit()

    return {
        'id': user.id,
        "access_token": access_token,
        "token_type": "bearer"
    }

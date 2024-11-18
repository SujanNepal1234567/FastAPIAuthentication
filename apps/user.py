import bcrypt
from fastapi import APIRouter, Depends, Header
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError

from apps.authentication import generate_user_token, valid_user, validate_refresh_token
from apps.models import User
from apps.schemas import (
    LoginResponseSchema,
    RefreshTokenResponseSchema,
    UserCreateSchema,
    UserLoginSchema,
    UserResponseSchema,
)
from db.session import get_session
from exceptions import INVALID_PASSWORD, USER_ALREADY_EXISTS, USER_NOT_FOUND

app = APIRouter()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/register-user", response_model=UserResponseSchema)
def singup(
    body: UserCreateSchema,
    db=Depends(get_session),
):
    body.password = bcrypt.hashpw(
        body.password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    user = User(
        name=body.name,
        email=body.email,
        location=body.location,
        about=body.about,
        password=body.password,
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise USER_ALREADY_EXISTS
    db.refresh(user)
    return user


@app.post("/auth/login", response_model=LoginResponseSchema)
def login(body: UserLoginSchema, db=Depends(get_session)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user:
        raise USER_NOT_FOUND
    verify_password = password_context.verify(body.password, user.password)
    if not verify_password:
        raise INVALID_PASSWORD
    response = generate_user_token(user.email)
    return response


@app.post("/auth/refresh-token", response_model=RefreshTokenResponseSchema)
def refresh_token(refresh_token: str = Header()):
    email = validate_refresh_token(refresh_token)
    access_token = generate_user_token(email)
    return {"access_token": access_token}


@app.get("/me", response_model=UserResponseSchema)
def me(
    Authorization: str = Header(),
    db=Depends(get_session),
):
    user = valid_user(Authorization)
    user_detail = User.get_user(user.get("user"), db)
    if not user_detail:
        raise USER_NOT_FOUND
    return user_detail

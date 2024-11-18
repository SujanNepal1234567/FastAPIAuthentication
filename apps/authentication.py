from datetime import datetime, timedelta, timezone
from time import time

from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from config import config
from exceptions import INVALID_REFRESH_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def generate_user_token(email) -> dict:
    payload = {
        "user": email,
        "exp": time() + config.access_token_expire * 60,
    }
    token = jwt.encode(payload, config.jwt_secret_key, algorithm=config.algorithm)
    refresh_token = create_refresh_token(payload)
    return {"access_token": token, "refresh_token": refresh_token}


def valid_user(token):
    if not token.startswith("Bearer "):
        raise INVALID_TOKEN
    token = token.split(" ")[1]
    try:
        payload = jwt.decode(
            token, config.jwt_secret_key, algorithms=[config.algorithm]
        )
        return payload
    except ExpiredSignatureError:
        raise TOKEN_EXPIRED
    except JWTError:
        raise INVALID_TOKEN


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=config.refresh_token_expire)
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode, config.jwt_refresh_secret_key, algorithm=config.algorithm
    )


def validate_refresh_token(refresh_token) -> str:
    try:
        # Decode and validate the refresh token
        payload = jwt.decode(
            refresh_token, config.jwt_refresh_secret_key, config.algorithm
        )
        email = payload.get("user")
        if email is None:
            raise INVALID_REFRESH_TOKEN
        return email
    except JWTError:
        raise INVALID_REFRESH_TOKEN

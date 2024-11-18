from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class BadRequest(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class NotFound(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)


class Unauthorized(BaseHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=401, detail=detail)


# TODO use seperate files
USER_NOT_FOUND = NotFound(detail="User not found")
INVALID_PASSWORD = BadRequest(detail="Invalid password")
USER_ALREADY_EXISTS = BadRequest(detail="User already exists")

INVALID_TOKEN = Unauthorized(detail="Invalid token")
TOKEN_EXPIRED = Unauthorized(detail="Token expired")
INVALID_REFRESH_TOKEN = Unauthorized(detail="Invalid refresh token")

from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    email: str
    location: str
    about: str
    password: str


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    location: str
    about: str
    created_at: str


class UserLoginSchema(BaseModel):
    email: str
    password: str


class RefreshTokenResponseSchema(BaseModel):
    access_token: str


class LoginResponseSchema(RefreshTokenResponseSchema):
    refresh_token: str

from fastapi import FastAPI
from apps.user import app as user_routes

app = FastAPI(
    title="FastAPI",
    description="FastAPI",
    version="1.0.0",
    contact={
        "name": "SujanNepal1234567",
    },
    root_path="/api/v1",
)

app.include_router(user_routes)

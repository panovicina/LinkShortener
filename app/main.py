from fastapi import FastAPI
from app.routers import router as link_router


def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(link_router)
    return app

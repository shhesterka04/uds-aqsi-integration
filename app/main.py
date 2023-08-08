from fastapi import FastAPI

from app.uds.router import router

app = FastAPI()

app.include_router(router)
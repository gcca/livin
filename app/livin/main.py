from fastapi import FastAPI
from livin.routers.auth import router as auth_router
from livin.routers.locations import router as locations_router
from livin.routers.users import router as users_router
from livin.routers.voyage import router as voyage_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(locations_router)
app.include_router(voyage_router)


@app.get("/")
def index() -> str:
    return "Welcome to Livin dots: ..."

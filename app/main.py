from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.auth_routes import router as auth_router
from app.api.leave_routes import router as leave_router

app = FastAPI(title="UMS Replica Backend")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(auth_router)
app.include_router(leave_router)


@app.get("/")
async def root():
    return {"status": "UMS Backend running 🚀"}
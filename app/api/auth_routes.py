from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.auth import RegisterSchema, LoginSchema
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(data: RegisterSchema, db: AsyncSession = Depends(get_db)):
    return await register_user(db, data)


@router.post("/login")
async def login(data: LoginSchema, db: AsyncSession = Depends(get_db)):
    tokens = await login_user(db, data)

    if not tokens:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return tokens
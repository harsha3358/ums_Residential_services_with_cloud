from sqlalchemy import select
from app.db import models
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)


async def register_user(db, data):
    user = models.User(
        name=data.name,
        registration_number=data.registration_number,
        password=hash_password(data.password),
        role=data.role,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user


async def login_user(db, data):
    result = await db.execute(
        select(models.User).where(
            models.User.registration_number == data.registration_number
        )
    )

    user = result.scalar_one_or_none()

    if not user:
        return None

    if not verify_password(data.password, user.password):
        return None

    payload = {
        "id": user.id,
        "role": user.role,
        "registration_number": user.registration_number,
    }

    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload),
    }
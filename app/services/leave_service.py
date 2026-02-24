from sqlalchemy import select
from app.db import models
import uuid


async def create_leave(db, user_id, data):
    leave = models.LeaveRequest(
        user_id=user_id,
        reason=data.reason,
        from_date=data.from_date,
        to_date=data.to_date,
    )

    db.add(leave)
    await db.commit()
    await db.refresh(leave)

    return leave


async def get_all_leaves(db):
    result = await db.execute(select(models.LeaveRequest))
    return result.scalars().all()


async def update_leave_status(db, leave_id, status):
    result = await db.execute(
        select(models.LeaveRequest).where(models.LeaveRequest.id == leave_id)
    )

    leave = result.scalar_one_or_none()

    if not leave:
        return None

    leave.status = status

    if status == "APPROVED":
        leave.qr_token = str(uuid.uuid4())

    await db.commit()
    return leave
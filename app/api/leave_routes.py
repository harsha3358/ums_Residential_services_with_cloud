from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.leave import LeaveCreate, LeaveApprove
from app.services.leave_service import (
    create_leave,
    get_all_leaves,
    update_leave_status,
)
from app.dependencies import get_current_user, require_role

router = APIRouter(prefix="/leave", tags=["Leave"])


@router.post("/")
async def apply_leave(
    data: LeaveCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user),
):
    return await create_leave(db, user["id"], data)


@router.get("/all")
async def list_leaves(
    db: AsyncSession = Depends(get_db),
    user=Depends(require_role("warden")),
):
    return await get_all_leaves(db)


@router.patch("/{leave_id}")
async def approve_leave(
    leave_id: int,
    data: LeaveApprove,
    db: AsyncSession = Depends(get_db),
    user=Depends(require_role("warden")),
):
    leave = await update_leave_status(db, leave_id, data.status)

    if not leave:
        raise HTTPException(status_code=404, detail="Leave not found")

    return leave
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    registration_number = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="student")


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reason = Column(Text)
    from_date = Column(String)
    to_date = Column(String)
    status = Column(String, default="PENDING")
    qr_token = Column(String, nullable=True)


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    message = Column(Text)
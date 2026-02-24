from pydantic import BaseModel


class RegisterSchema(BaseModel):
    name: str
    registration_number: str
    password: str
    role: str = "student"


class LoginSchema(BaseModel):
    registration_number: str
    password: str
from pydantic import BaseModel, EmailStr, SecretStr, Field


class UserRegisterResponse(BaseModel):
    first_name: str
    last_name: str


class UserLoginResponse(BaseModel):
    email: EmailStr = Field(..., min_length=10)
    password: SecretStr = Field(..., min_length=8, max_length=64)



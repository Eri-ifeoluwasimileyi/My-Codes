from pydantic import BaseModel, EmailStr, SecretStr, Field


class UserRegisterRequest(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(..., min_length=10)
    password: SecretStr = Field(..., min_length=8, max_length=64)


class UserLoginRequest(BaseModel):
    email: EmailStr = Field(..., min_length=10)
    password: SecretStr = Field(..., min_length=8, max_length=64)



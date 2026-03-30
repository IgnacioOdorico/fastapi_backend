from pydantic import BaseModel, Field, EmailStr

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=3, example="Juan Perez")
    email: EmailStr
    edad: int = Field(..., gt=0, example=25)

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None
    edad: int | None = Field(default=None, gt=0)

class ClienteResponse(ClienteBase):
    id: int
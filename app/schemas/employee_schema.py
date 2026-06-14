from pydantic import BaseModel, EmailStr, Field
from datetime import date

class EmployeeCreate(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    email: EmailStr
    puesto: str = Field(..., max_length=50)
    salario: float = Field(..., gt=0)
    fecha_ingreso: date

class EmployeeUpdate(BaseModel):
    nombre: str | None = Field(None, max_length=100)
    apellido: str | None = Field(None, max_length=100)
    email: EmailStr | None = None
    puesto: str | None = Field(None, max_length=50)
    salario: float | None = Field(None, gt=0)
    fecha_ingreso: date | None = None

class EmployeeResponse(BaseModel):
    id: str
    nombre: str
    apellido: str
    email: str
    puesto: str
    salario: float
    fecha_ingreso: date
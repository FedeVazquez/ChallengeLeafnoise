from fastapi import APIRouter, Query, status, Depends

from app.services.employee_service import EmployeeService
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.core.security import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    dependencies=[Depends(get_current_user)]
)
service = EmployeeService()


@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate):
    return service.create_employee(employee)


@router.get("/", response_model=list[EmployeeResponse])
def get_employees(
    puesto: str | None = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
):
    return service.get_employees(puesto, page, limit)


@router.get("/stats/salary-average")
def get_average_salary():
    return {"average_salary": service.get_average_salary()}


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee_by_id(employee_id: str):
    return service.get_employee_by_id(employee_id)


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: str, employee: EmployeeUpdate):
    return service.update_employee(employee_id, employee)


@router.delete("/{employee_id}")
def delete_employee(employee_id: str):
    return {"deleted": service.delete_employee(employee_id)}
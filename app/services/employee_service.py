from fastapi import HTTPException
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def create_employee(self, employee: EmployeeCreate) -> dict:
        # Verificar si ya existe un empleado con el mismo email
        existing_employee = self.repository.find_by_email(employee.email)
        if existing_employee:
            raise HTTPException(status_code=409, detail="Email already exists")

        # Crear el empleado
        return self.repository.create(employee.model_dump())

    def get_employees(self, puesto: str | None, page: int, limit: int) -> list[dict]:
        return self.repository.find_all(puesto, page, limit)

    def get_employee_by_id(self, employee_id: str) -> dict:
        employee = self.repository.find_by_id(employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    def update_employee(self, employee_id: str, employee: EmployeeUpdate) -> dict:
        # Ignorar campos None
        update_data = employee.model_dump(exclude_none=True)

        updated_employee = self.repository.update(employee_id, update_data)
        if not updated_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return updated_employee

    def delete_employee(self, employee_id: str) -> bool:
        deleted = self.repository.delete(employee_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Employee not found")
        return deleted

    def get_average_salary(self) -> float:
        return self.repository.get_average_salary()
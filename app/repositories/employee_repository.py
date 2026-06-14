from datetime import date, datetime, time

from bson import ObjectId
from bson.errors import InvalidId
from pymongo.collection import Collection
from pymongo import ReturnDocument

from app.database.mongo import get_database


class EmployeeRepository:
    def __init__(self):
        self.collection: Collection = get_database()["employees"]

    def _serialize_employee(self, employee: dict) -> dict:
        employee["id"] = str(employee["_id"])
        employee.pop("_id", None)
        return employee

    def _prepare_employee_data(self, employee_data: dict) -> dict:
        if isinstance(employee_data.get("fecha_ingreso"), date):
            employee_data["fecha_ingreso"] = datetime.combine(
                employee_data["fecha_ingreso"],
                time.min
            )

        return employee_data

    def create(self, employee_data: dict) -> dict:
        employee_data = self._prepare_employee_data(employee_data)

        result = self.collection.insert_one(employee_data)
        created_employee = self.collection.find_one({"_id": result.inserted_id})

        return self._serialize_employee(created_employee)

    def find_all(
        self,
        puesto: str | None = None,
        page: int = 1,
        limit: int = 10
    ) -> list[dict]:
        query = {}

        if puesto:
            query["puesto"] = puesto

        skip = (page - 1) * limit

        employees = self.collection.find(query).skip(skip).limit(limit)

        return [self._serialize_employee(employee) for employee in employees]

    def find_by_id(self, employee_id: str) -> dict | None:
        try:
            employee = self.collection.find_one({"_id": ObjectId(employee_id)})

            if not employee:
                return None

            return self._serialize_employee(employee)

        except InvalidId:
            return None

    def find_by_email(self, email: str) -> dict | None:
        employee = self.collection.find_one({"email": email})

        if not employee:
            return None

        return self._serialize_employee(employee)

    def update(self, employee_id: str, employee_data: dict) -> dict | None:
        try:
            employee_data = self._prepare_employee_data(employee_data)

            updated_employee = self.collection.find_one_and_update(
                {"_id": ObjectId(employee_id)},
                {"$set": employee_data},
                return_document=ReturnDocument.AFTER
            )

            if not updated_employee:
                return None

            return self._serialize_employee(updated_employee)

        except InvalidId:
            return None

    def delete(self, employee_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(employee_id)})
            return result.deleted_count > 0

        except InvalidId:
            return False

    def get_average_salary(self) -> float:
        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "average_salary": {"$avg": "$salario"}
                }
            }
        ]

        result = list(self.collection.aggregate(pipeline))

        if not result:
            return 0.0

        return float(result[0]["average_salary"])
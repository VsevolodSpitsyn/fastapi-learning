
from fastapi import APIRouter, status, HTTPException

from .crud import storage
from .schemas import Employee, EmployeeCreate

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("", response_model = list[Employee])
def get_employees_list() -> list[Employee]:
    return storage.get_employees_list()


@router.get("/{employee_id}", response_model = Employee, responses={status.HTTP_404_NOT_FOUND: {
                "description": "Employee not found",
                "content": {
                    "application/json": {
                      "schema": {
                        "title": "Not found",
                          "type": "object",
                          "properties": {
                            "detail": {
                              "title": "Detail",
                                "type": "string",
                                "example": "Employee #123 not found",
                            },
                          },
                      },
                    },
                },
            },
        },
                      )
def get_employee_by_id(employee_id: int) -> Employee:
    employee = storage.get_employee_by_id(employee_id = employee_id)
    if employee is not None:
        return employee
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Employee #{employee_id} not found")


@router.post("", response_model=Employee, status_code= status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate) -> Employee:
    return storage.create_employee(employee=employee)


@router.delete("/{employee_id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int) -> None:
    storage.delete_employee_by_id(employee_id = employee_id)
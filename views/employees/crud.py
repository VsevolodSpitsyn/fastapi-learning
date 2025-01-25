"""
C - create
R - read
U - update
D - delete
"""
from dataclasses import dataclass, field

from .schemas import Employee, EmployeeCreate


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int, Employee] = field(default_factory=dict)

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id


    def create_employee(self, employee: EmployeeCreate) -> Employee:
        new_employee = Employee(id = self.next_id, **employee.model_dump())
        self.employees[new_employee.id] = new_employee
        return new_employee


    def get_employees_list(self) -> list[Employee]:
        return list(self.employees.values())


    def get_employee_by_id(self, employee_id: int) -> Employee | None:
        return self.employees.get(employee_id)


    def delete_employee_by_id(self, employee_id: int) -> None:
        self.employees.pop(employee_id, None)



storage = EmployeeStorage()






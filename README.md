# FastAPI Learning

## Description
This is a learning web application developed using FastAPI. The project implements a REST API for managing employee data.

### Core technologies:
- **FastAPI**: Fast and simple web application development.
- **Pydantic**: Used for data validation and schema management.
- **Dataclasses**: For in-memory data storage.
- **Git**: Code is published on GitHub.

---

## Features
The application provides the following functionality:
1. Create a new employee (POST).
2. Retrieve a list of all employees (GET).
3. Get details of a specific employee by their ID (GET).
4. Delete an employee by their ID (DELETE).

Interactive API documentation is available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Installation and Usage

### 1. Install dependencies
You need Python 3.9 or higher to run the application. Make sure `pip` is installed and run the following commands:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```



Project Structure
```bash
fastapi-learning/
├── main.py                     # Main application file
├── requirements.txt            # Project dependencies
├── views/                      # Main API handlers
│   ├── __init__.py             # Views package
│   ├── api.py                  # Top-level router
│   └── employees/              # Employee-specific logic
│       ├── __init__.py
│       ├── api.py              # API request handlers
│       ├── crud.py             # CRUD operations for employees
│       └── schemas.py          # Pydantic schemas for validation
└── .gitignore                  # List of files and folders excluded from the repository
```

API Endpoints

1. Get a list of employees
	•	Method: GET
	•	URL: /api/employees
	•	Description: Returns a list of all employees.
	•	Example Response:
```json
[
  {
    "id": 1,
    "full_name": "John Doe",
    "email": "john.doe@example.com"
  }
]
```
2. Create a new employee
	•	Method: POST
	•	URL: /api/employees
	•	Description: Creates a new employee.
	•	Example Request:
```json
{
  "full_name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```
Example Response:
```json
{
  "id": 2,
  "full_name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```
3. Get an employee by ID
	•	Method: GET
	•	URL: /api/employees/{employee_id}
	•	Description: Returns details of an employee by their ID.
	•	Example Success Response (Status 200):
```json
{
  "id": 1,
  "full_name": "John Doe",
  "email": "john.doe@example.com"
}
```
Example Error Response (Status 404):
```json
{
  "detail": "Employee not found"
}
```
4. Delete an employee by ID
	•	Method: DELETE
	•	URL: /api/employees/{employee_id}
	•	Description: Deletes an employee by their ID.
	•	Example Success Response:
Status 204 No Content.


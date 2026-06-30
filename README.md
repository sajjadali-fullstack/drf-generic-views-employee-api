# Employee API — Django REST Framework Generic Views

A clean Employee Management API built with DRF's **Generic Views**, 
showing how much boilerplate you can eliminate compared to plain `APIView`.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-red?style=flat&logo=django&logoColor=white)

---

## Why Generic Views?

| Approach | Lines of Code | Control |
|---|---|---|
| `APIView` (manual) | 15+ | Full control |
| `ListAPIView` / `CreateAPIView` | 3-4 | Less boilerplate |

This project shows both — the manual version is kept commented in the code 
as a reference.

---

## API Endpoints

| Endpoint | Method | View | Description |
|---|---|---|---|
| `/api/` | GET | `EmployeeListAPIView` | List all employees |
| `/api-create/` | POST | `EmployeeCreateAPIView` | Create a new employee |

---

## Employee Model

| Field | Type |
|---|---|
| employee_id | Integer |
| first_name, last_name | CharField |
| email | CharField |
| gender | CharField |
| address | CharField |
| date_of_birth | DateField |
| salary | FloatField |
| position, department | CharField |
| created_at, updated_at | DateTimeField (auto) |

---

## Admin Panel

Registered with custom `EmployeeAdmin`:
- **list_display:** employee_id, first_name, salary, created_at
- **search_fields:** first_name, salary, address
- **list_filter:** gender, department

---

## Tech Stack

- Python
- Django
- Django REST Framework

---



## Screenshots

### GET /api/
![GET Employees](screenshots/get-employees.png)

### POST /api-create/
![Create Employee](screenshots/create-employee.png)

---

## Author

**Sajjad Ali** — [GitHub](https://github.com/sajjadali-fullstack) ·
[Portfolio](https://sajjadali-fullstack-portfolio.netlify.app/)

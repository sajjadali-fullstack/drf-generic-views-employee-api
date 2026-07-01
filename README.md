# Employee API — Django REST Framework Generic Views (Full CRUD)

A complete Employee Management REST API built with DRF's **Generic Views**.
Full CRUD — List, Create, Retrieve, Update, and Delete — with minimal code.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-red?style=flat&logo=django&logoColor=white)

---

## Why Generic Views?

| Approach | Lines of Code | Boilerplate |
|---|---|---|
| `APIView` (manual) | 15+ per endpoint | High |
| Generic Views | 3-4 per endpoint | Almost zero |

This project includes both approaches — the manual `APIView` version is
kept commented in the code as a learning reference.

---

## API Endpoints

| Endpoint | Method | View | Description |
|---|---|---|---|
| `/api/` | GET | `EmployeeListAPIView` | List all employees |
| `/api-create/` | POST | `EmployeeCreateAPIView` | Create new employee |
| `/api-retrieve/<int:id>` | GET | `EmployeeRetrieveAPIView` | Get single employee |
| `/api-update/<int:id>` | PUT / PATCH | `EmployeeUpdateView` | Update employee |
| `/api-destroy/<int:id>` | DELETE | `EmployeeDestroyView` | Delete employee |

---

## Employee Model

| Field | Type | Notes |
|---|---|---|
| employee_id | IntegerField | Manual ID |
| first_name | CharField | max 50 |
| last_name | CharField | max 49 |
| email | CharField | max 100 |
| gender | CharField | max 1 |
| address | CharField | max 99 |
| date_of_birth | DateField | — |
| salary | FloatField | — |
| position | CharField | max 50 |
| department | CharField | max 50 |
| created_at | DateTimeField | auto on create |
| updated_at | DateTimeField | auto on update |


---

---

## Views — How It Works

```python
# 3 lines = full retrieve logic
class EmployeeRetrieveView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
```

DRF Generic Views handle automatically:
- queryset fetching
- serialization
- response building
- error handling
- status codes

---

## Serializer

```python
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
```

---

## Admin Panel

```python
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'first_name', 'salary', 'created_at']
    search_fields = ['first_name', 'salary', 'address']
    list_filter = ['gender', 'department']
```

---

## Screenshots

### GET /api/ — List All Employees
![GET All](screenshots/get-all.png)

### POST /api-create/ — Create Employee
![POST](screenshots/post-create.png)

### GET /api-retrieve/1 — Single Employee
![GET Single](screenshots/get-single.png)

### PUT /api-update/1 — Update Employee
![PUT](screenshots/put-update.png)

### DELETE /api-destroy/1 — Delete Employee
![DELETE](screenshots/delete.png)


---

## What's Next

- [ ] Combine all 5 views into one using `ModelViewSet`
- [ ] Add authentication to protect endpoints
- [ ] Add pagination

---

## Author

**Sajjad Ali** — [GitHub](https://github.com/sajjadali-fullstack) ·
[Portfolio](https://sajjadali-fullstack-portfolio.netlify.app/)
---

## Project Structure

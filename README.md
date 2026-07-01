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

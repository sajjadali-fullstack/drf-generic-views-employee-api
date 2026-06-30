from django.db import models

# Create your models / SQL Table here.

class Employee(models.Model):
    # employee_id, first_name, last_name, email, gender, date_of_birth, salary, position, department, created_at, updated_at
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=49)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=99)
    date_of_birth = models.DateField()
    salary = models.FloatField()
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
# API with models
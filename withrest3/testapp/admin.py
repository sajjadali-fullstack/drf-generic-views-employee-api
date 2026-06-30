from django.contrib import admin
from testapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'first_name', 'salary', 'created_at']
    search_fields = ['first_name', 'salary', 'address']
    list_filter = ['gender', 'department']

# Register your models here.
admin.site.register(Employee)
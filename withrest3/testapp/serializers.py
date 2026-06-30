from rest_framework.serializers import ModelSerializer
from testapp.models import Employee

# In modelserilizers --> Very less line of code required 
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


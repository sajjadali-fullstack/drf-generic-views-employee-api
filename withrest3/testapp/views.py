# from django.shortcuts import render
# from testapp.models import Employee
# from testapp.serializers import EmployeeSerializer

# Response class convert Dictionary into JSON 🌟
# from rest_framework.response import  Response
# from rest_framework.views import APIView


# Create your views / business logic here👇.

#                             OPTON - 1 😊


# class EmployeeListAPIView(APIView):

#     def get(self, request):
#         query_set = Employee.objects.all()  # Multipal Employee Details
#         # querySet we have to convert into serializer 🌟
#         serializer = EmployeeSerializer(query_set, many=True)
#         return Response(serializer.data)


#                             OPTON - 2 😍


from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

# Create your views / business logic here. 👇

# For GET Request
class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer   
        

# For CREATE Request
class EmployeeCreateAPIView(CreateAPIView):
    queryset= Employee.objects.all()
    serializer_class = EmployeeSerializer


# For Retrive Request
class EmployeeRetriveView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


#  For Update Request
class EmployeeUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class  = EmployeeSerializer
    lookup_field = 'id'

# For Destroy Request
class EmployeeDestroyView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


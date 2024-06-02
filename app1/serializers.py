from rest_framework.serializers import ModelSerializer
from .models import *

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model= Employee
        # Exclude empId from the fields to be serialized
        #fields = ['empName', 'mobile', 'email', 'pancard']
        exclude = ['empId']

class StudentSerializer(ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'
        
class PatientSerializer(ModelSerializer):
    class Meta:
        model= Patient
        fields='__all__'

class LabSerializer(ModelSerializer):
    class Meta:
        model= Lab
        fields='__all__'
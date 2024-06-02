from django.shortcuts import render
from .models import *

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import *

class getAllEmployees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
class getEmployeeById(APIView):
    def get(self, request, empId):
        try:
            employee = Employee.objects.get(empId=empId)
        except Employee.DoesNotExist:
            raise Http404
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class createEmployee(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee has been created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class updateEmployee(APIView):
    def put(self, request, empId):
        try:
            employee = Employee.objects.get(empId=empId)
        except Employee.DoesNotExist:
            raise Http404

        serializer = EmployeeSerializer(employee, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee has been updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class deleteEmployee(APIView):
    def delete(self, request, empId):
        try:
            employee = Employee.objects.get(empId=empId)
        except Employee.DoesNotExist:
            raise Http404

        employee.delete()
        return Response({"message": "Employee has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#Student 

class getAllStudents(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class getStudentById(APIView):
    def get(self, request, stdId):
        try:
            student = Student.objects.get(stdId=stdId)
        except Student.DoesNotExist:
            raise Http404
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class createStudent(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student has been created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class updateStudent(APIView):
    def put(self, request, stdId):
        try:
            student = Student.objects.get(stdId=stdId)
        except Student.DoesNotExist:
            raise Http404

        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student has been updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class deleteStudent(APIView):
    def delete(self, request, stdId):
        try:
            student = Student.objects.get(stdId=stdId)
        except Student.DoesNotExist:
            raise Http404

        student.delete()
        return Response({"message": "Student has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#Patient

class getAllPatients(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
class getPatientById(APIView):
    def get(self, request, patientId):
        try:
            patient = Patient.objects.get(patientId=patientId)
        except Patient.DoesNotExist:
            raise Http404
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


class createPatient(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient has been created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class updatePatient(APIView):
    def put(self, request, patientId):
        try:
            patient = Patient.objects.get(patientId=patientId)
        except Patient.DoesNotExist:
            raise Http404

        serializer = PatientSerializer(patient, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient has been updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class deletePatient(APIView):
    def delete(self, request, patientId):
        try:
            patient = Patient.objects.get(patientId=patientId)
        except Patient.DoesNotExist:
            raise Http404

        patient.delete()
        return Response({"message": "Patient has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


#Lab

class getAllLabs(APIView):
    def get(self, request):
        labs = Lab.objects.all()
        serializer = LabSerializer(labs, many=True)
        return Response(serializer.data)
    
class getLabById(APIView):
    def get(self, request, labId):
        try:
            lab = Lab.objects.get(labId=labId)
        except Lab.DoesNotExist:
            raise Http404
        serializer = LabSerializer(lab)
        return Response(serializer.data)


class createLab(APIView):
    def post(self, request):
        serializer = LabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab has been created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class updateLab(APIView):
    def put(self, request, labId):
        try:
            lab = Lab.objects.get(labId=labId)
        except Lab.DoesNotExist:
            raise Http404

        serializer = LabSerializer(lab, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lab has been updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class deleteLab(APIView):
    def delete(self, request, labId):
        try:
            lab = Lab.objects.get(labId=labId)
        except Lab.DoesNotExist:
            raise Http404

        lab.delete()
        return Response({"message": "Lab has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


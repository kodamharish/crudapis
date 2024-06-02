from django.urls import path
from .views import *

urlpatterns = [
    #Employee
    path('employee/create/',createEmployee.as_view(),name='employee-create'),
    path('employees/',getAllEmployees.as_view(),name='employee-all'),
    path('employee/id/<str:empId>/',getEmployeeById.as_view(),name='employee-by-id'),
    path('employee/update/<str:empId>/',updateEmployee.as_view(),name='employee-update'),
    path('employee/delete/<str:empId>/',deleteEmployee.as_view(),name='employee-delete'),

    #Student
    path('student/create/',createStudent.as_view(),name='student-create'),
    path('students/',getAllStudents.as_view(),name='student-all'),
    path('student/id/<str:stdId>/',getStudentById.as_view(),name='student-by-id'),
    path('student/update/<str:stdId>/',updateStudent.as_view(),name='student-update'),
    path('student/delete/<str:stdId>/',deleteStudent.as_view(),name='student-delete'),

    #Patient
    path('patient/create/',createPatient.as_view(),name='patient-create'),
    path('patients/',getAllPatients.as_view(),name='patient-all'),
    path('patient/id/<str:patientId>/',getPatientById.as_view(),name='patient-by-id'),
    path('patient/update/<str:patientId>/',updatePatient.as_view(),name='patient-update'),
    path('patient/delete/<str:patientId>/',deletePatient.as_view(),name='patient-delete'),

    #Lab
    path('lab/create/',createLab.as_view(),name='lab-create'),
    path('labs/',getAllLabs.as_view(),name='lab-all'),
    path('lab/id/<str:labId>/',getLabById.as_view(),name='lab-by-id'),
    path('lab/update/<str:labId>/',updateLab.as_view(),name='lab-update'),
    path('lab/delete/<str:labId>/',deleteLab.as_view(),name='lab-delete'),

]

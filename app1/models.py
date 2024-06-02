from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class EmployeeIDSequence(models.Model):
    current_id = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.current_id)
    
class Employee(models.Model):
    empId=models.CharField(max_length=10,primary_key=True,editable=False)
    empName=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.EmailField()
    pancard=models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.empId:
            sequence, created = EmployeeIDSequence.objects.get_or_create(pk=1)
            sequence.current_id += 1
            self.empId = f'EMP{sequence.current_id:03d}'
            sequence.save()
        super(Employee, self).save(*args, **kwargs)
    def __str__(self):
        return self.empId

class Student(models.Model):
    stdId=models.CharField(max_length=10,primary_key=True)
    stdName=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.EmailField()

class Patient(models.Model):
    patientId=models.CharField(max_length=100,primary_key=True)
    patientName=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    doctorName=models.CharField(max_length=100)

from django.db.models import Max
class Lab(models.Model):
    labId=models.CharField(max_length=100,primary_key=True)
    patientId=models.CharField(max_length=100,unique=True)
    #patientId = models.IntegerField(unique=True, editable=False)
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    patientName=models.CharField(max_length=100)
    testName=models.CharField(max_length=100)
    # def save(self, *args, **kwargs):
    #     if not self.patientId:
    #         last_patient = Lab.objects.order_by('-patientId').first()
    #         if last_patient:
    #             self.patientId = last_patient.patientId + 1
    #         else:
    #             self.patientId = 1
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.name} - {self.patientId}"
    # def save(self, *args, **kwargs):
    #     if not self.patientId:
    #         max_id = Lab.objects.aggregate(max_id=Max('patientId'))['max_id']
    #         self.patientId = (max_id or 0) + 1
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.name} - {self.patientId}"


    
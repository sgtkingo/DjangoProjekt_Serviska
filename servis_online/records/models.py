from django.db import models
from datetime import datetime

# Create your models here.

class Record(models.Model):
    timestamp = models.DateTimeField(default=datetime.now())
    device_info = models.CharField(max_length=50)
    device_error = models.CharField(max_length=100)
    servis_solution = models.ForeignKey("Solution", on_delete=models.SET_NULL, blank=True, null=True)
    person_info = models.ForeignKey("Person",on_delete=models.CASCADE)
    DEVICE_TYPES = [
        ('NTB', 'Notebook'),
        ('PC', 'Computer'),
        ('SMP', 'SmartPhone'),
        ('TBL', 'Tablet'),
        ('OT', 'Other'),
    ]
    device_type = models.CharField(max_length=4,choices=DEVICE_TYPES,default="NON")

    def __str__(self):
        return "{} {} [{}]".format(self.device_info,self.person_info,self.timestamp)

    def getSolutionDescription(self):
        return self.servis_solution

    def getPersonDescription(self):
        return self.person_info.getDescription()

    def isSoluted(self):
        return self.servis_solution.isOK()

class Person(models.Model):
    person_name = models.CharField(max_length=30)
    person_address = models.CharField(max_length=100)
    person_contact = models.CharField(max_length=50)
    person_phone = models.BigIntegerField()

    def __str__(self):
        return self.person_name

    def getDescription(self):
        return "Name: {} / Phone: {} \n Contact: {}  / {}".format(self.person_name,self.person_phone,self.person_address,self.person_contact)

class Solution(models.Model):
    solution_description=models.CharField(max_length=100)
    solution_cost=models.IntegerField()
    solution_ok=models.BooleanField()

    SOLUTION_TYPE = [
        ('HW_REP', 'Hardware Repair'),
        ('HW_CHG', 'Hardware Change'),
        ('SW_RES', 'Software Reinstall'),
        ('SW_REP', 'Software Repair'),
        ('OTHER', 'Other repair'),
    ]
    solution_type = models.CharField(max_length=6,choices=SOLUTION_TYPE,default="NON")

    def __str__(self):
        return "{} (cost: {}) -> [{}]".format(self.solution_description,self.solution_cost,self.solution_type)

    def isOK(self):
        return self.solution_ok
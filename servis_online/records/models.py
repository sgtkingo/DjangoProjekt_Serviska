from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as lazy

# Create your models here.

class Record(models.Model):
    timestamp = models.DateTimeField(default=datetime.now())
    device_info = models.CharField(max_length=50)
    device_problem = models.CharField(max_length=100)
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

    def getProblemDescription(self):
        return "Device: {} -> {}".format(self.device_info,self.device_problem)

    def getSolutionDescription(self):
        if self.servis_solution is not None:
            return self.servis_solution
        else:
            return "No solution yet..."
    def getSolutionMaterials(self):
        if self.servis_solution is not None:
            return self.servis_solution.getMaterials()
        else:
            return "---"
    def getSolutionBalance(self):
        if self.servis_solution is not None:
            return self.servis_solution.getBalance()
        else:
            return "-"
    def getPersonDescription(self):
        if self.person_info is not None:
            return self.person_info.getDescription()
        else:
            return "No person added!"

    def isSoluted(self):
        if self.servis_solution is not None:
            return self.servis_solution.isOK()
        else:
            return "false"

class Person(models.Model):
    person_name = models.CharField(max_length=30)
    person_address = models.CharField(max_length=100)
    person_contact = models.EmailField(max_length=50)
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
    solution_materials=models.ManyToManyField("Material")

    def __str__(self):
        return "{} (cost: {},- Kc) -> [{}]".format(self.solution_description,self.solution_cost,self.solution_type)

    def isOK(self):
        return self.solution_ok

    def getMaterials(self):
        return self.solution_materials

    def getBalance(self):
        sum=0
        for item in self.solution_materials.all():
            sum=sum+item.material_cost
        return (self.solution_cost-sum)

class Material(models.Model):
    material_name=models.CharField(max_length=50)
    material_info=models.CharField(max_length=50)
    MATERIAL_TYPE = [
        ('NEW', 'New material'),
        ('REPAS', 'Repas material'),
        ('SOFT', 'Software material'),
        ('OTHER', 'Other material'),
    ]
    material_type = models.CharField(max_length=5,choices=MATERIAL_TYPE,default="NON")
    material_cost=models.IntegerField()

    def __str__(self):
        return "{} ({} -> {},- Kc) [{}]".format(self.material_name,self.material_info,self.material_cost,self.material_type)

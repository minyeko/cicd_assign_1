from django.db import models
from students.models import Student

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
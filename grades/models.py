# models.py in your Django app
from django.db import models
from students.models import Student

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)  # Assuming grades are given as letters like A, B, C, etc.

    def __str__(self):
        return f"{self.student} - {self.course_name} - {self.grade}"

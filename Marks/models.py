# marks/models.py
from django.db import models
from students.models import Student

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    mark = models.FloatField()
    
    def __str__(self):
        return f"{self.student} - {self.course_name}: {self.mark}"

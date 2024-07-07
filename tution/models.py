from django.db import models
from students.models import Student

# Create your models here.
class Tution(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    

    def __str__(self):
        return f"{self.amount_due} - {self.due_date} - {self.student}"
    
from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in months

    def __str__(self):
        return self.name
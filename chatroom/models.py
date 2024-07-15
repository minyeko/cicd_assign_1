from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(User, related_name='chatrooms')

    def __str__(self):
        return self.name

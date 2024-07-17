from django.contrib.auth.models import User
from rest_framework import serializers
from chatroom.models import Chatroom


class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['id', 'name', 'created_at', 'updated_at', 'members']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
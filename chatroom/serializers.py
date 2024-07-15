from rest_framework import serializers

from chatroom.models import Chatroom


class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['id', 'name', 'created_at', 'updated_at', 'members']
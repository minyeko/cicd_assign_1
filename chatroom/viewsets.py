from rest_framework import viewsets

from chatroom.models import Chatroom
from chatroom.serializers import ChatroomSerializer


class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer

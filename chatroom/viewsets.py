from django.contrib.auth.models import User
from rest_framework import viewsets
from chatroom.models import Chatroom
from chatroom.serializers import ChatroomSerializer, UserSerializer


class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

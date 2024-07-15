from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chatroom.viewsets import ChatroomViewSet

router = DefaultRouter()
router.register(r'chatroom', ChatroomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

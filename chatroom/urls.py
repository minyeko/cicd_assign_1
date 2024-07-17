from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chatroom.viewsets import ChatroomViewSet, UserViewSet


router = DefaultRouter()
router.register(r'chatroom', ChatroomViewSet)
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]

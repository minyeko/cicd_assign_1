from django.urls import path, include
from . import views
from .views import LectureViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lectures', LectureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.lecturer_list, name='lecturer_list'),
]

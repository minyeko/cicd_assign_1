
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecturer_list, name='lecturer_list'),
]


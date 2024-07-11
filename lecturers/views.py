from django.shortcuts import render
from .models import lecture
from rest_framework import viewsets
from .serializers import LectureSerializer

def lecturer_list(request):
    lecturers = lecture.objects.all()
    return render(request, 'lecturers/lecturer_list.html', {'lecturers': lecturers})
# Create your views here. Test


class LectureViewSet(viewsets.ModelViewSet):
    queryset = lecture.objects.all()
    serializer_class = LectureSerializer

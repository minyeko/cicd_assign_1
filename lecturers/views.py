from django.shortcuts import render
from .models import lecture

def lecturer_list(request):
    lecturers = lecture.objects.all()
    return render(request, 'lecturers/lecturer_list.html', {'lecturers': lecturers})
# Create your views here. Test

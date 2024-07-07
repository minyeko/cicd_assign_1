from django.shortcuts import render
from .models import Program

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})
# Create your views here.

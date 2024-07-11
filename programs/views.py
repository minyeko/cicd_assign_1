from django.shortcuts import render
from rest_framework import viewsets
from .models import Program
from .serializers import ProgramSerializer

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})
# Create your views here.

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

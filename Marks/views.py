from rest_framework import viewsets
from .models import Mark
from .serializers import MarkSerializer

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

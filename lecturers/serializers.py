from rest_framework import serializers
from .models import lecture

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = lecture
        fields = '__all__'

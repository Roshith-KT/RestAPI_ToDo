from . models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Task
        fields="__all__"
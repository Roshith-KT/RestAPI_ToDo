from django.shortcuts import render
from . models import Task
from . serializers import TaskSerializer
from rest_framework import viewsets
# Create your views here.


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer

class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().filter(completed=False).order_by('created_at')
    serializer_class=TaskSerializer
from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Project class"""

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for the Task class"""

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComponentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Component class"""

    queryset = models.Component.objects.all()
    serializer_class = serializers.ComponentSerializer
    permission_classes = [permissions.IsAuthenticated]



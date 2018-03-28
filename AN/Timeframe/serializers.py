from . import models

from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'contact', 
            'due', 
        )


class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Component
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'notes', 
        )



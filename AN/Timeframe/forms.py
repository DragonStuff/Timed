from django import forms
from .models import Project, Task, Component, Sum


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'contact', 'due', 'author', 'project', 'time_spent', 'completed']


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'notes', 'task', 'time_spent', 'completed']



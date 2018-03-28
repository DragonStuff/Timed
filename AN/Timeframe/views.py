from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Project, Task, Component, Sum
from .forms import ProjectForm, TaskForm, ComponentForm


class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm


class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm


class ComponentListView(ListView):
    model = Component


class ComponentCreateView(CreateView):
    model = Component
    form_class = ComponentForm


class ComponentDetailView(DetailView):
    model = Component


class ComponentUpdateView(UpdateView):
    model = Component
    form_class = ComponentForm


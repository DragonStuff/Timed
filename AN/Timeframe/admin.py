from django.contrib import admin
from django import forms
from .models import Project, Task, Component

class ProjectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Project, ProjectAdmin)


class TaskAdminForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'contact', 'due']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'contact', 'due']

admin.site.register(Task, TaskAdmin)


class ComponentAdminForm(forms.ModelForm):

    class Meta:
        model = Component
        fields = '__all__'


class ComponentAdmin(admin.ModelAdmin):
    form = ComponentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'notes']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'notes']

admin.site.register(Component, ComponentAdmin)



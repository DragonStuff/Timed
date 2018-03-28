from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Project(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    # None ATM

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '%s' % (self.name)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Timeframe_project_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Timeframe_project_update', args=(self.slug,))


class Task(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    contact = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    due = models.DateField()
    time_spent = models.IntegerField(null=True, blank=True)
    completed = models.BooleanField()

    # Relationship Fields
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%s' % (self.name)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Timeframe_task_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Timeframe_task_update', args=(self.slug,))

class Component(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    notes = models.TextField(max_length=500)
    time_spent = models.IntegerField(null=True, blank=True)
    completed = models.BooleanField()

    # Relationship Fields
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ('completed', '-created')

    def __str__(self):
        return '%s - %s' % (self.task, self.name)
        
    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Timeframe_component_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Timeframe_component_update', args=(self.slug,))
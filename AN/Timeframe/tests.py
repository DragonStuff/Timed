import unittest
from django.urls import reverse
from django.test import Client
from .models import Project, Task, Component
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_project(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "tasks" not in defaults:
        defaults["tasks"] = create_task()
    return Project.objects.create(**defaults)


def create_task(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["contact"] = "contact"
    defaults["due"] = "due"
    defaults.update(**kwargs)
    if "components" not in defaults:
        defaults["components"] = create_component()
    if "author" not in defaults:
        defaults["author"] = create_django_contrib_auth_models_user()
    return Task.objects.create(**defaults)


def create_component(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["notes"] = "notes"
    defaults.update(**kwargs)
    return Component.objects.create(**defaults)


class ProjectViewTest(unittest.TestCase):
    '''
    Tests for Project
    '''
    def setUp(self):
        self.client = Client()

    def test_list_project(self):
        url = reverse('Timeframe_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_project(self):
        url = reverse('Timeframe_project_create')
        data = {
            "name": "name",
            "tasks": create_task().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_project(self):
        project = create_project()
        url = reverse('Timeframe_project_detail', args=[project.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_project(self):
        project = create_project()
        data = {
            "name": "name",
            "tasks": create_task().pk,
        }
        url = reverse('Timeframe_project_update', args=[project.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TaskViewTest(unittest.TestCase):
    '''
    Tests for Task
    '''
    def setUp(self):
        self.client = Client()

    def test_list_task(self):
        url = reverse('Timeframe_task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        url = reverse('Timeframe_task_create')
        data = {
            "name": "name",
            "contact": "contact",
            "due": "due",
            "components": create_component().pk,
            "author": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_task(self):
        task = create_task()
        url = reverse('Timeframe_task_detail', args=[task.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        task = create_task()
        data = {
            "name": "name",
            "contact": "contact",
            "due": "due",
            "components": create_component().pk,
            "author": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('Timeframe_task_update', args=[task.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ComponentViewTest(unittest.TestCase):
    '''
    Tests for Component
    '''
    def setUp(self):
        self.client = Client()

    def test_list_component(self):
        url = reverse('Timeframe_component_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_component(self):
        url = reverse('Timeframe_component_create')
        data = {
            "name": "name",
            "notes": "notes",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_component(self):
        component = create_component()
        url = reverse('Timeframe_component_detail', args=[component.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_component(self):
        component = create_component()
        data = {
            "name": "name",
            "notes": "notes",
        }
        url = reverse('Timeframe_component_update', args=[component.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



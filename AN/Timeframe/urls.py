from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'project', api.ProjectViewSet)
router.register(r'task', api.TaskViewSet)
router.register(r'component', api.ComponentViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Project
    path('Timeframe/project/', views.ProjectListView.as_view(), name='Timeframe_project_list'),
    path('Timeframe/project/create/', views.ProjectCreateView.as_view(), name='Timeframe_project_create'),
    path('Timeframe/project/detail/<slug:slug>/', views.ProjectDetailView.as_view(), name='Timeframe_project_detail'),
    path('Timeframe/project/update/<slug:slug>/', views.ProjectUpdateView.as_view(), name='Timeframe_project_update'),
)

urlpatterns += (
    # urls for Task
    path('Timeframe/task/', views.TaskListView.as_view(), name='Timeframe_task_list'),
    path('Timeframe/task/create/', views.TaskCreateView.as_view(), name='Timeframe_task_create'),
    path('Timeframe/task/detail/<slug:slug>/', views.TaskDetailView.as_view(), name='Timeframe_task_detail'),
    path('Timeframe/task/update/<slug:slug>/', views.TaskUpdateView.as_view(), name='Timeframe_task_update'),
)

urlpatterns += (
    # urls for Component
    path('Timeframe/component/', views.ComponentListView.as_view(), name='Timeframe_component_list'),
    path('Timeframe/component/create/', views.ComponentCreateView.as_view(), name='Timeframe_component_create'),
    path('Timeframe/component/detail/<slug:slug>/', views.ComponentDetailView.as_view(), name='Timeframe_component_detail'),
    path('Timeframe/component/update/<slug:slug>/', views.ComponentUpdateView.as_view(), name='Timeframe_component_update'),
)


from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('project/<str:project_id>', views.project, name='project'),
]
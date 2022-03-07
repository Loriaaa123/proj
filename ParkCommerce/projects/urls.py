from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects/<str:project_id>', views.project, name='project'),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:object_id>', views.updateProject, name='update-project'),
    path('delete-project/<str:object_id>', views.deleteProject, name='delete-project'),
]


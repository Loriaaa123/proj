from multiprocessing import context
from tkinter import N
from tkinter.messagebox import NO
from django.shortcuts import render
from .models import Project, Review, Tag

def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    projectObj = Project.objects.get(id=project_id)
    tags = projectObj.tag.all()
    context = {"project": projectObj, "tags": tags}
    return render(request, 'projects/project.html', context)

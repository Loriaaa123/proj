from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    projectObj = Project.objects.get(id=project_id)
    tags = projectObj.tags.all()
    context = {"project": projectObj, "tags": tags}
    return render(request, 'projects/project.html', context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def updateProject(request, object_id):
    project = Project.objects.get(id=object_id)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, object_id):
    project = Project.objects.get(id=object_id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
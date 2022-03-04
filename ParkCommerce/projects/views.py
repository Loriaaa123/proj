from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request)
    # custom_range, projects, paginator = paginateProjects(request, projects, 10)
    projects, paginator = paginateProjects(request, projects, 10)
    # context = {"projects": projects, "search_query": search_query, 'paginator': paginator, 'custom_range': custom_range}
    context = {"projects": projects, "search_query": search_query, 'paginator': paginator}
    return render(request, 'projects/projects.html', context)

def project(request, project_id):
    projectObj = Project.objects.get(id=project_id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount()

        messages.success(request, 'Review submitted successfully')
        return redirect('project', project_id=project_id)
    # update votecount
    tags = projectObj.tags.all()
    context = {"project": projectObj, "tags": tags, 'form': form}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form': form, 'profile': profile}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, object_id):
    profile = request.user.profile
    project = profile.project_set.get(id=object_id)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form, 'profile': profile, 'project': project}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, object_id):
    profile = request.user.profile
    project = profile.project_set.get(id=object_id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)
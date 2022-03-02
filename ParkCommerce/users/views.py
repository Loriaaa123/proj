from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Skill
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import searchProfiles, paginateProfiles


def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles, paginator = paginateProfiles(request, profiles, 3)
    context = { "profiles": profiles, "search_query": search_query, "custom_range": custom_range, "paginator": paginator }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skills.exclude(description__exact='')
    other_skills = profile.skills.filter(description='')
    context = { "profile": profile , "topSkills": top_skills, "otherSkills": other_skills }
    return render(request, 'users/user-profile.html', context)

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User not found")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have successfully registered')           
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Invalid form')
            return redirect('register')
    context = { "page": page , "form": form }
    return render(request, 'users/login_register.html', context)

def inbox(request):
    return render(request, 'users/inbox.html')

@login_required
def userAccount(request):
    profile = request.user.profile 

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)

@login_required
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('account')
        else:
            messages.error(request, 'Invalid form')
            return redirect('edit-account')
    context = {}
    return render(request, 'users/profile_form.html', context)

@login_required
def createSkill(request):
    profile =  request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Your skill has been added')
            return redirect('account')
        else:
            messages.error(request, 'Invalid form')
            return redirect('create-skill')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

@login_required
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your skill has been updated')
            return redirect('account')
        else:
            messages.error(request, 'Invalid form')
            return redirect('edit-skill')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

@login_required
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Your skill has been deleted')
        return redirect('account')
    context = {'skill': skill}
    return render(request, 'users/delete_skill.html', context)
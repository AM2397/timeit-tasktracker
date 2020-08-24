from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, ProjectForm, TaskForm, TimerForm
from .models import TaskMaster, ProjectMaster


# Authentication & Authorization Views
@unauthenticated_user
def newregistration(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='sys_user')
            user.groups.add(group)

            messages.success(
                request, 'Account Successfully Created for ' + username)

            return redirect('loginuser')

    context = {'form': form}
    return render(request, 'tasktracker/register.html', context)


@unauthenticated_user
def loginuser(request):
    template = 'tasktracker/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request.session['name'] = username

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            if user.groups.filter(name='sys_user').exists():
                return redirect(addorupdatetask)
            elif user.groups.filter(name='admin').exists():
                return redirect(addorupdateproject)
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('loginuser')
    return render(request, template)


def logoutuser(request):
    logout(request)
    return redirect('loginuser')


# User Specific Views
@login_required(login_url='loginuser')
@allowed_users(allowed_roles='sys_user')
def listalltasks(request):
    context = {'task_list': TaskMaster.objects.all()}
    return render(request, "tasktracker/tasklist.html", context)


@login_required(login_url='loginuser')
@allowed_users(allowed_roles='sys_user')
def addorupdatetask(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TaskForm()
        else:
            task = TaskMaster.objects.get(pk=id)
            form = TaskForm(instance=task)
        return render(request, "tasktracker/addorupdatetask.html", {'form': form})
    else:
        if id == 0:
            form = TaskForm(request.POST)
        else:
            task = TaskMaster.objects.get(pk=id)
            form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
        return redirect('/listalltasks')


@login_required(login_url='loginuser')
@allowed_users(allowed_roles='sys_user')
def deletetask(request, id):
    task = TaskMaster.objects.get(pk=id)
    task.delete()
    return redirect('/listalltasks')


@login_required(login_url='loginuser')
@allowed_users(allowed_roles='sys_user')
def timetask(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TimerForm()
        else:
            task = TaskMaster.objects.get(pk=id)
            form = TimerForm(instance=task)
        return render(request, "tasktracker/tasktimer.html", {'form': form})
    else:
        if id == 0:
            form = TimerForm(request.POST)
        else:
            task = TaskMaster.objects.get(pk=id)
            form = TimerForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
        return redirect('/listalltasks')


# Admin Specific Views
@login_required(login_url='loginuser')
@allowed_users(allowed_roles='admin')
def listallprojects(request):
    context = {'projects_list': ProjectMaster.objects.all()}
    return render(request, "tasktracker/projectlist.html", context)


@login_required(login_url='loginuser')
@allowed_users(allowed_roles='admin')
def addorupdateproject(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProjectForm()
        else:
            project = ProjectMaster.objects.get(pk=id)
            form = ProjectForm(instance=project)
        return render(request, "tasktracker/addorupdateproject.html", {'form': form})
    else:
        if id == 0:
            form = ProjectForm(request.POST)
        else:
            project = ProjectMaster.objects.get(pk=id)
            form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
        return redirect('/listallprojects')


@login_required(login_url='loginuser')
@allowed_users(allowed_roles='admin')
def deleteproject(request, id):
    project = ProjectMaster.objects.get(pk=id)
    project.delete()
    return redirect('/listallprojects')

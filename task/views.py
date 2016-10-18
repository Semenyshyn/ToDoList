from django.shortcuts import render_to_response, redirect, render
from .models import Task
from django.contrib import auth
from .forms import TaskForm
from datetime import datetime


def tasks(request):
    return render_to_response('tasks.html', {'tasks': Task.objects.all(), 'username': auth.get_user(request).username})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_from_id = request.user.id
            task.pub_date = datetime.now()
            task.save()
            return redirect('/', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form, 'username': auth.get_user(request).username})


def delete(request, task_id):
    obj = Task.objects.get(pk=task_id)
    obj.delete()
    return redirect('/')
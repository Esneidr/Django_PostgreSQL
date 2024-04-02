from django.shortcuts import render, redirect
from .models import Taks

# Create your views here.
def list_tasks(request):
    tasks = Taks.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks })

def create_task(request):
    task = Taks(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Taks.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')


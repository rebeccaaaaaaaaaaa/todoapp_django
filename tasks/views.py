from django.forms.forms import Form
import tasks
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
def index(request):
    #chamar todas as tasks do bd para o template
    tasks = Task.objects.all().order_by('-created_at')
    
    #retornar a view para mostrar no front
    return render(request, 'tasks/list.html', {'tasks' : tasks})


def taskView(request, id):
    task =  get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task' : task})



def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'Task add successfully.')
            return redirect('/')
    else:
        form = TaskForm()
        return render (request, 'tasks/newtask.html', {'form' : form})


def editView(request, id):
    task =  get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    
    if (request.method == 'POST'):
       form = TaskForm(request.POST, instance=task)
       
       if form.is_valid():
           task.save()
           messages.info(request, 'Task updated successfully.')
           return redirect('/')
       else:
            return render(request, 'tasks/edittask.html', {'form' : form, 'task' : task})
        
    else:
        return render(request, 'tasks/edittask.html', {'form' : form, 'task' : task})
    
def deleteView(request, id):
    task =  get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Task deleted successfully.')
    return redirect('/')
   
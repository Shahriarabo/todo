from django.shortcuts import render,redirect
from .models import Task


# Create your views here.


def index(request):
    # saving task
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        is_done = request.POST.get("is_done")
        if is_done == "no":
            is_done = "True"

        else:
            is_done = "False"

        tasks = Task(name=title, description=description, is_done=is_done)
        tasks.save()

    # randering
    task = Task.objects.all()
    context = {'task': task}

    return render(request, 'index.html', context)


def edit(request,task_id):
     #updating the task
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        title = request.POST.get("title")        
        description = request.POST.get("description")        
        is_done = request.POST.get("is_done")
        if is_done == "on":
            is_done = "True"
        else:
            is_done = "False"
        task.name = title
        task.description = description
        task.is_done = is_done
        
        task.save()
        
        return redirect('/')

    #rendaring the page
    task = Task.objects.get(id=task_id)
    context = {'id':task.id,'title':task.name, 'description':task.description, 'is_done':task.is_done}
    return render(request, 'edit.html',context)

def delete(request,task_id):
    #deleting task
    if request.method == "GET":
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')
         #rendaring the page
        task = Task.objects.get(id=task_id)
        context = {'id':task.id,'title':task.name, 'description':task.description, 'is_done':task.is_done}
    return render(request, 'delete.html')

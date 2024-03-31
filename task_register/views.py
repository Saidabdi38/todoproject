from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def task_list(request):
     if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=Task.objects.raw('select id, fullname, tel, zoone, creation_date, due_date, completion, memo from task_register_task where creation_date between "'+fromdate+'" and  "'+todate+'"') 
        return render(request, "task_register/task_list.html", {"task_list":searchresult})
     else:
        context = Task.objects.all().order_by('id')
        return render(request,"task_register/task_list.html",{'task_list':context})

@login_required
def task_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = TaskForm()
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(instance=task)
        return render(request,"task_register/task_form.html",{'form':form})
    else:
        if id == 0:
            form = TaskForm(request.POST)
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/task/list')

@login_required
def not_complete(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=Task.objects.raw('select id, fullname, tel, zoone, creation_date, due_date, completion, memo from task_register_task where creation_date between "'+fromdate+'" and "'+todate+'" and completion="Not Completed"') 
        return render(request, "task_register/task_list.html", {"task_list":searchresult})
    else:
        context = {'task_list':Task.objects.all().filter(completion='Not Completed').order_by('id')}
        return render(request,"task_register/not_complete.html",context)

def searchtask(request):
    context = {'task_list':Task.objects.get().filter(tel='tel')}
    return render(request,"task_register/task_list.html",context)

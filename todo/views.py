from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login_view')
def home(request):
    if request.method == 'POST':
        username = request.user
        titlename = request.POST.get('title')
        description = request.POST.get('desc')
        priority_choice = request.POST.get('option')
        TodoItem.objects.create(user = username, title = titlename, desc = description, priority = priority_choice)
        return redirect('/')
        
    data = TodoItem.objects.filter(user = request.user)
    return render(request, 'home.html', {'data' : data})

#deleting the task here
def DeleteTask(request, task_id):
    TodoItem.objects.get(id = task_id).delete()
    return redirect('/')

#updating the task
def UpDateTask(request, task_id):

    if request.method == 'POST':
        t = TodoItem.objects.get(id = task_id)
        t.user = request.user
        t.title = request.POST.get('title')
        t.desc = request.POST.get('desc')
        t.priority = request.POST.get('option')
        t.save()
        return redirect('/')

    print(task_id)

    data = TodoItem.objects.filter(user = request.user)
    onetask = TodoItem.objects.get(id = task_id)
    print(onetask.title)
    return render(request, 'home.html', {'onetask' : onetask, 'data':data})


#registering the user
def registration(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'forms' : form})


#login the user
def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    #print("It is not working bro")
    return render(request, 'login.html', {'form' : form})
 

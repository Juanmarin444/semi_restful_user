from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# from django.utils import timezone

def index(request):
    # response = "Django server is up and running."
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'crud_users/users.html',context)

def show(request, id):
    # response = "Placeholder for Showing User # " + id + "."
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, 'crud_users/show_user.html', context)

def edit(request, id):
    context = {"id":id}
    return render(request, 'crud_users/edit_user.html', context)

def edit_user(request, id):
    user = User.objects.get(id=id)
    user.full_name = request.POST['name']
    user.email = request.POST['email']
    user.save()
    return redirect('/')

def add_user(request):
    return render(request, 'crud_users/add_user.html')

def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
       for tag, error in errors.items():
          messages.error(request, error, extra_tags=tag)
       return redirect('/add_user')
    else:
        User.objects.create(full_name = request.POST['name'], email = request.POST['email'])
    return redirect('/')

def destroy(request, id):
    user_to_delete = User.objects.get(id=id)
    user_to_delete.delete()
    return redirect('/')

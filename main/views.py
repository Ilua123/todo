from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import Todo
# Create your views here.

def todo(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'index.html', context)

def create_todo(request):
    new_todo=Todo()
    if request.method == 'POST':
        new_todo.title = request.POST.get('name')
        new_todo.description = request.POST.get('zametka')
        new_todo.save()
        return  HttpResponseRedirect('/')
    return  HttpResponseRedirect('/')

def delete_record(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect('/')

def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'todo':todo})

def read(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'read.html', {'todo':todo})
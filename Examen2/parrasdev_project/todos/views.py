from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('todo_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

# CRUD
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})

def todos_ids(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_ids.html", {"todos": todos})

def todos_ids_titles(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_ids_titles.html", {"todos": todos})

def todos_resueltos(request):
    todos = Todo.objects.filter(is_done=True)
    return render(request, "todos/todo_resueltos.html", {"todos": todos})

def todos_no_resueltos(request):
    todos = Todo.objects.filter(is_done=False)
    return render(request, "todos/todo_no_resueltos.html", {"todos": todos})

def todos_ids_user(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_ids_user.html", {"todos": todos})

def todos_resueltos_user(request):
    todos = Todo.objects.filter(is_done=True)
    return render(request, "todos/todo_resueltos_user.html", {"todos": todos})

def todos_no_resueltos_user(request):
    todos = Todo.objects.filter(is_done=False)
    return render(request, "todos/todo_no_resueltos_user.html", {"todos": todos})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
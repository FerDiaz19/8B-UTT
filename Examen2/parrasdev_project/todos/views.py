from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# CRUD
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/list.html", {"todos": todos})

def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    return render(request, "todos/form.html", {"form": form})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("todo_list")
    return render(request, "todos/form.html", {"form": form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list")
    return render(request, "todos/confirm_delete.html", {"todo": todo})

# Listas especiales
def todos_ids(request):
    todos = Todo.objects.values_list("id", flat=True)
    return render(request, "todos/list.html", {"todos": todos})

def todos_ids_titles(request):
    todos = Todo.objects.values("id", "title")
    return render(request, "todos/list.html", {"todos": todos})

def todos_resueltos(request):
    todos = Todo.objects.filter(is_done=True).values("id", "title")
    return render(request, "todos/list.html", {"todos": todos})

def todos_no_resueltos(request):
    todos = Todo.objects.filter(is_done=False).values("id", "title")
    return render(request, "todos/list.html", {"todos": todos})

def todos_ids_user(request):
    todos = Todo.objects.values("id", "user_id")
    return render(request, "todos/list.html", {"todos": todos})

def todos_resueltos_user(request):
    todos = Todo.objects.filter(is_done=True).values("id", "user_id")
    return render(request, "todos/list.html", {"todos": todos})

def todos_no_resueltos_user(request):
    todos = Todo.objects.filter(is_done=False).values("id", "user_id")
    return render(request, "todos/list.html", {"todos": todos})
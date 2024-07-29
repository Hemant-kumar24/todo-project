from django.shortcuts import render,redirect
from .models import Todo,Profile
# Create your views here.
def home(request):
    return render(request,"home.html")
def todo(request):
    result=Todo.objects.all()
    incompleted_todos=[]
    completed_todos=[]
    for todo in result:
        if todo.is_completed != True:
            incompleted_todos.append(todo)
        else:
            completed_todos.append(todo)
    parameter={"todos":incompleted_todos,
               "completed_todos":completed_todos,}
    return render(request,"todo.html",parameter)
def add_todo(request):
    if request.method=="POST":
        task=request.POST.get("task")
        date=request.POST.get("date")
        new_todo=Todo(task=task,date=date)
        new_todo.save()
        return redirect("todo")
    return render(request,"add_todo.html")
def delete(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo")
def update_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    if request.method=="POST":
        task=request.POST.get("task")
        date=request.POST.get("date")
        todo.task=task
        todo.date=date
        todo.save()
        return redirect("todo")
    parameter={'todo':todo
               }
    return render(request,"update_todo.html",parameter)

def about(request):
    return render(request,"about.html")
def complete(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.is_completed = True
    todo.save()
    return redirect ("todo")
def profile(request):
    if request.method =="POST":
        profile_pic=request.FILES["profile_pic"]
        new_profile=Profile(
            title="demo",
            profile_pic=profile_pic
        )
        new_profile.save()
        return redirect("todo")
    return render(request,"profile.html")

    
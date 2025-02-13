from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('is_complete')  # Order tasks by completion status
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == "POST":  # if the request is post then it will create the task
        title = request.POST.get('title')  # gets the title, note data from html form temp
        note = request.POST.get('note')
        Task.objects.create(title=title, note=note)  # passing the data to the task class model like we did in CRUD operation
        return redirect('task_list')  # after creating the task it will redirect to the task_list page
    return render(request, 'todo_app/task_create.html')  # if the request is not post then it will render repeat the task_create.html page

def task_update(request, slug):
    task = get_object_or_404(Task, slug=slug)  # getting the task by slug
    if request.method == "POST":
        title = request.POST.get('title')  # getting the title from the form
        note = request.POST.get('note')  # getting the note from the form
        is_complete = request.POST.get('is_complete') == 'on'  # getting the is_complete from the form
        task.title = title  # updating the title
        task.note = note  # updating the note
        task.is_complete = is_complete  # updating the is_complete
        task.save()  # saving the updated data
        return redirect('task_list')  # redirecting to the task_list page
    return render(request, 'todo_app/task_update.html', {'task': task})  # if the request is not post then it will render the task_update.html page

def task_delete(request, slug):
    task = get_object_or_404(Task, slug=slug)  # getting the task by slug
    if request.method == "POST" and request.POST.get('confirm_delete') == 'on':
        task.delete()  # deleting the task
        return redirect('task_list')  # redirecting to the task_list page
    return render(request, 'todo_app/task_delete.html', {'task': task})  # if the request is not post then it will render the task_delete.html page

def task_toggle_complete(request, slug):
    task = get_object_or_404(Task, slug=slug)  # getting the task by slug
    task.is_complete = not task.is_complete
    task.save()
    return redirect('task_list')
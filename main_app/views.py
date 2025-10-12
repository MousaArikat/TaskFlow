from django.shortcuts import render, redirect
from .forms import TaskForm
from django.urls import reverse, reverse_lazy



# Create your views here.
def home_page(request):
    return render(request, 'main_app/homepage.html')


def create_task(request):
    if request.method == "POST":
        form = TaskForm()
        if form.is_valid():
            task = form.save()
            return redirect(reverse('task_list'))
        else:
            return render(request, 'main_app/task-list.html', {'form' : form})
    elif request.method == "POST":
        form = TaskForm()
        return render(request, 'main_app/task-list.html', {'form' : form})

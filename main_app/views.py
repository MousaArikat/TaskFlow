from django.shortcuts import render, redirect
from .forms import TaskForm
from django.urls import reverse, reverse_lazy
from .models import Task
from django.views.generic import DetailView



# Create your views here.
def home_page(request):
    return render(request, 'main_app/homepage.html')


def list_tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'main_app/task-list.html', {'tasks_list': tasks_list})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect(reverse('task_list'))
        else:
            return render(request, 'main_app/create-task.html', {'form' : form})
    elif request.method == "GET":
        form = TaskForm()
        return render(request, 'main_app/create-task.html', {'form' : form})

class task_details_view(DetailView):
    model = Task
    template_name = "main_app/task-details.html"
    context_object_name = "task"
    pk_url_kwarg = "id"
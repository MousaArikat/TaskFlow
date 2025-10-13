from django.shortcuts import render, redirect
from .forms import TaskForm, QuestForm
from django.urls import reverse, reverse_lazy
from .models import Task, Quest
from django.views.generic import DetailView, DeleteView, UpdateView



# Create your views here.
def home_page(request):
    return render(request, 'main_app/homepage.html')

def list_quests(request):
    quest_list = Quest.objects.all()
    return render(request, 'main_app/quest-list.html', {'quest_list' : quest_list})

def list_tasks(request):
    task_list = Task.objects.all()
    return render(request, 'main_app/task-list.html', {'tasks_list': task_list})



def create_quest(request):
    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            quest = form.save()
            return redirect(reverse("quest_list"))
        else:
            return render(request, "main_app/create-quest.html", {"form" : form})
    elif request.method == "GET":
        form = QuestForm()
        return render(request, "main_app/create-quest.html", {"form" : form})











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

def update_task(request, id):
    task = Task.objects.get(pk = id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            task = form.save()
            return redirect(reverse("task_list"))
        else: 
            return render(request, 'main_app/create-task.html', {'form' : form})
    elif request.method == "GET":
        form = TaskForm(instance = task)
        return render(request, "main_app/create-task.html", {"form" : form})





class task_delete_view(DeleteView):
    model = Task
    pk_url_kwarg = "id"
    success_url = reverse_lazy("task_list")


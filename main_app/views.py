from django.shortcuts import render, redirect
from .forms import TaskForm, QuestForm, CustomUserCreationForm
from django.urls import reverse, reverse_lazy
from .models import Task, Quest
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
class Home(LoginView):
    template_name = 'main_app/homepage.html'

def about_page(request):
    return render(request, 'main_app/about.html')

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

class quest_details_view(DetailView):
    model = Quest
    template_name = "main_app/quest-details.html"
    context_object_name = "quest"
    pk_url_kwarg = "quest_id"

def list_quests(request):
    quest_list = Quest.objects.all()
    return render(request, 'main_app/quest-list.html', {'quest_list' : quest_list})


def list_tasks(request):
    task_list = Task.objects.all()
    return render(request, 'main_app/task-list.html', {'tasks_list': task_list})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            quest_id = task.quest.quest_id
            return redirect(reverse('view_quest', kwargs = {"quest_id": quest_id}))
        else:
            return render(request, 'main_app/create-task.html', {'form' : form})
    elif request.method == "GET":
        form = TaskForm()
        return render(request, 'main_app/create-task.html', {'form' : form})

class task_details_view(DetailView):
    model = Task
    template_name = "main_app/task-details.html"
    context_object_name = "task"
    pk_url_kwarg = "task_id"



def update_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            task = form.save()
            quest_id = task.quest.quest_id
            return redirect(reverse("view_quest", kwargs = {"quest_id" : quest_id}))
        else: 
            return render(request, 'main_app/create-task.html', {'form' : form})
    elif request.method == "GET":
        form = TaskForm(instance = task)
        return render(request, "main_app/create-task.html", {"form" : form})

class task_delete_view(DeleteView):
    model = Task
    pk_url_kwarg = "task_id"
    
    def get_success_url(self):
        quest_id = self.object.quest.quest_id
        return reverse_lazy('view_quest', kwargs = {'quest_id' : quest_id})

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
        else:
            error_message = 'Invalid Sign Up - please try again!'
    elif request.method == "GET":
        form = CustomUserCreationForm
        context = {"form" : form, 'error_message' : error_message}
        return render(request, 'main_app/signup.html', context)
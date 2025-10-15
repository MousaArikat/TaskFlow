from django.shortcuts import render, redirect
from .forms import TaskForm, QuestForm, CustomUserCreationForm
from django.urls import reverse, reverse_lazy
from .models import Task, Quest, UserProfile, Rank
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

def view_achievments(request):
    return render(request, "main_app/achievments.html")

# Create your views here.
@login_required
def dashboard_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    xp = profile.total_xp

    if xp>=15000:
        rank = Rank.objects.get(title = "S-RANK MASTER: THE SHADOW MONARCH")
        current_min = 15000
        next_min = None
    elif xp >= 8000:
        rank = Rank.objects.get(title = "A-RANK ELITE: ELITE HUNTER")
        current_min = 8000
        next_min = 15000
    elif xp >= 4000:
        rank = Rank.objects.get(title = "B-RANK EXPERT: THE PHANTOM HUNTER")
        current_min = 4000
        next_min = 8000
    elif xp >= 2000:
        rank = Rank.objects.get(title = "C-RANK ADEPT: APEX HUNTER")
        current_min = 2000
        next_min = 4000
    elif xp >= 500:
        rank = Rank.objects.get(title = "D-RANK NOVICE: MANA HUNTER")
        current_min = 500
        next_min = 2000
    else:
        rank = Rank.objects.get(title = "E-RANK ROOKIE: AWAKENED HUNTER")
        current_min = 0
        next_min = 500

    if profile.rank != rank:
        profile.rank = rank
        profile.save()
    
    if next_min:
        rank_progress = ((xp-current_min)/ (next_min - current_min) * 100)
    else:
        rank_progress = 100

    active_quests = Quest.objects.filter(user=request.user)[:3]
    quests_progress = []
    for quest in active_quests:
        total_tasks = quest.task_set.count()
        completed_tasks = quest.task_set.filter(is_completed = True).count()

        progress = 0
        if total_tasks > 0:
            quest_progress = round((completed_tasks / total_tasks) * 100)
        else:
            quest_progress = 0
        
        quests_progress.append({
            "id" : quest.quest_id,
            "title" : quest.title,
            "progress": quest_progress,
        })

    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'main_app/dashboard.html', {'active_quests' : quests_progress, 
                                                       'profile' : profile, 
                                                       'rank_progress' : round(rank_progress,1), 
                                                       'current_min' : current_min, 
                                                       'next_min' : next_min})
    




def about_page(request):
    return render(request, 'main_app/about.html')



@login_required
def create_quest(request):
    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            quest = form.save(commit = False)
            quest.user = request.user
            quest.save()
            return redirect(reverse("quest_list"))
        else:
            return render(request, "main_app/create-quest.html", {"form" : form})
    elif request.method == "GET":
        form = QuestForm()
        return render(request, "main_app/create-quest.html", {"form" : form})
class quest_details_view(LoginRequiredMixin, DetailView):
    model = Quest
    template_name = "main_app/quest-details.html"
    context_object_name = "quest"
    pk_url_kwarg = "quest_id"

    def get_queryset(self):
        return Quest.objects.filter(user = self.request.user)


@login_required
def list_quests(request):
    quest_list = Quest.objects.filter(user = request.user)
    quest_list = request.user.quest_set.all()
    return render(request, 'main_app/quest-list.html', {'quest_list' : quest_list})





@login_required
def list_tasks(request):
    task_list = Task.objects.all()
    return render(request, 'main_app/task-list.html', {'tasks_list': task_list})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        form.fields['quest'].queryset = Quest.objects.filter(user=request.user)
        if form.is_valid():
            task = form.save()
            quest_id = task.quest.quest_id
            return redirect(reverse('view_quest', kwargs = {"quest_id": quest_id}))
        else:
            return render(request, 'main_app/create-task.html', {'form' : form})
    elif request.method == "GET":
        form = TaskForm()
        form.fields['quest'].queryset = Quest.objects.filter(user=request.user)
        return render(request, 'main_app/create-task.html', {'form' : form})
class task_details_view(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "main_app/task-details.html"
    context_object_name = "task"
    pk_url_kwarg = "task_id"

    def get_queryset(self):
        return Task.objects.filter(quest__user = self.request.user)


@login_required
def update_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    if task.quest.user != request.user:
        raise Http404("This task doesn't belong to you, player!")

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        form.fields['quest'].queryset = Quest.objects.filter(user=request.user)
        if form.is_valid():
            task = form.save()
            quest_id = task.quest.quest_id
            return redirect(reverse("view_quest", kwargs = {"quest_id" : quest_id}))
        else: 
            return render(request, 'main_app/create-task.html', {'form' : form})
    elif request.method == "GET":
        form = TaskForm(instance = task)
        form.fields['quest'].queryset = Quest.objects.filter(user=request.user)
        return render(request, "main_app/create-task.html", {"form" : form})



class task_delete_view(LoginRequiredMixin,DeleteView):
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
            return render(request, 'main_app/signup.html', {"form" : form, 'error_message' : error_message})
    elif request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, 'main_app/signup.html', {"form" : form, 'error_message' : error_message})
    

@login_required
def mark_task_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.quest.user != request.user:
        raise Http404("You cannot complete tasks that aren't yours!")
    
    if not task.is_completed:

        task.is_completed = True
        task.save()

        profile = UserProfile.objects.get(user= request.user)

        if task.difficulty == "easy":
            profile.total_xp += 50
        elif task.difficulty == "medium":
            profile.total_xp += 100
        elif task.difficulty == "hard":
            profile.total_xp += 200
        profile.save(())
    return redirect('view_quest', quest_id=task.quest.quest_id)

@login_required
def update_quest(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    if quest.user != request.user:
        raise Http404("This quest doesn't belong to you, player!")

    if request.method == "POST":
        form = QuestForm(request.POST, instance=quest)
        if form.is_valid():
            form.save()
            return redirect('view_quest', quest_id=quest.quest_id)
        else:
            return render(request, "main_app/create-quest.html", {"form": form})
    elif request.method == "GET":
        form = QuestForm(instance=quest)
        return render(request, "main_app/create-quest.html", {"form": form})


@login_required
def delete_quest(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)
    if quest.user != request.user:
        raise Http404("This quest doesn't belong to you, player!")

    if request.method == "POST":
        quest.delete()
        return redirect('quest_list')
    else:
        return redirect('view_quest', quest_id=quest_id)


@login_required
@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    xp = profile.total_xp

    # Determine current and next rank thresholds
    if xp >= 15000:
        current_min = 15000
        next_min = None
    elif xp >= 8000:
        current_min = 8000
        next_min = 15000
    elif xp >= 4000:
        current_min = 4000
        next_min = 8000
    elif xp >= 2000:
        current_min = 2000
        next_min = 4000
    elif xp >= 500:
        current_min = 500
        next_min = 2000
    else:
        current_min = 0
        next_min = 500

    if next_min:
        rank_progress = ((xp - current_min) / (next_min - current_min)) * 100
    else:
        rank_progress = 100

    return render(request, "main_app/user-profile.html", {
        "user": request.user,
        "profile": profile,
        "rank_progress": round(rank_progress, 1),
        "current_min": current_min,
        "next_min": next_min
    })


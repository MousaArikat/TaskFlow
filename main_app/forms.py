from django import forms 
from .models import Task, Quest


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_id','title','description','difficulty', 'deadline', 'quest']


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['quest_id', 'title', 'description', 'category']

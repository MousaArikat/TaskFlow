from django import forms 
from .models import Task, Quest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_id','title','description','difficulty', 'deadline', 'quest']
        error_messages = {
            'title':{
                'max_length': 'Please keep the length less than 50 characters'
            },
            'deadline': {
                'invalid': "Please enter a valid date in the format MM/DD/YYYY.",
            }
        }


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['quest_id', 'title', 'description', 'category']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length = 30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

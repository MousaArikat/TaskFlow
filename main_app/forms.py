from django import forms 
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_id','title','description','category','difficulty','is_completed', 'deadline']
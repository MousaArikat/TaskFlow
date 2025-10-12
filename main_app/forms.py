from django import forms 
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_id','title','description','category','difficulty','is_completed', 'deadline']
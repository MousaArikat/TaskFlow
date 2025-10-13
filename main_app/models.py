from django.db import models
from django.contrib.auth.models import User


categories = [
    ('mix', 'Mix'),
    ('study', 'Study'), 
    ('fitness','Fitness'),
    ('work','Work'),
    ('habit','Habit'),
    ('daily routine','Daily Routine'),
    ('self care','Self Care'),
    ('other','Other')
    ]

difficulties = [

    ('easy', 'Easy'), 
    ('medium', 'Medium'), 
    ('hard', 'Hard')
    ]

# Create your models here.

class Quest(models.Model):
    quest_id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    category = models.CharField(max_length = 40, 
                                choices = categories, 
                                default = categories[0][0])
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Task(models.Model):
    task_id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    difficulty = models.CharField(max_length = 30, choices = difficulties)
    reward_xp = models.IntegerField(null = True)
    is_completed = models.BooleanField(default = False)
    date_created = models.DateTimeField(null = True)
    deadline = models.DateTimeField()
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    total_xp = models.IntegerField(default = 0)
    rank = models.CharField(max_length= 40)
    streak_days = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

from django.db import models

# Create your models here.
class Tasks(models.Model):
    quest_id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    category = models.CharField(max_length = 40, choices = [('study', 'Study'), ('fitness','Fitness'),('work','Work'),('habit','Habit'),('daily routine','Daily Routine'),('self care','Self Care'),('other','Other')])
    difficulty = models.CharField(max_length = 30, choices = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    reward_xp = models.IntegerField()
    is_completed = models.BooleanField(default = False)
    date_created = models.DateTimeField()
    deadline = models.DateTimeField()
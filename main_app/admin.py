from django.contrib import admin
from .models import Quest, Task, Rank, Achievment, UserProfile

# Register your models here.
admin.site.register(Quest)
admin.site.register(Task)
admin.site.register(Rank)
admin.site.register(Achievment)
admin.site.register(UserProfile)

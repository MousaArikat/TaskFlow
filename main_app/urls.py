from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('list', views.list_tasks, name = 'task_list'),
    path('create', views.create_task, name = 'create_task'),
    path('quests/view', views.list_quests, name = "quest_list"),
    path('quests/create', views.create_quest, name = "create_quest"),
    path("quests/<int:quest_id>", views.quest_details_view.as_view(), name = "view_quest"),
    path('quests/<int:quest_id>/tasks/<int:task_id>', views.task_details_view.as_view(), name = "view_task"),
    path('tasks/<int:task_id>/update', views.update_task, name = 'update_task'),
    path('tasks/<int:task_id>/delete', views.task_delete_view.as_view(), name = "delete_task"),
]

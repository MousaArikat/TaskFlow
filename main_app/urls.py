from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('list', views.list_tasks, name = 'task_list'),
    path('create', views.create_task, name = 'create_task')
]

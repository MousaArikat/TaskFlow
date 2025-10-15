from django.urls import path, include
from . import views
from django.contrib.auth import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', v.LoginView.as_view(template_name = "main_app/login.html"), name = "login"),
    path('logout/', v.LogoutView.as_view(next_page = 'login'), name = "logout"),
    path('', views.dashboard_view ,name = 'homepage'),
    path('achievments/', views.view_achievments, name = "view_achievments"),
    path('about/', views.about_page, name = 'about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name = 'signup'),
    path('list', views.list_tasks, name = 'task_list'),
    path('create', views.create_task, name = 'create_task'),
    path('quests/view', views.list_quests, name = "quest_list"),
    path('quests/create', views.create_quest, name = "create_quest"),
    path("quests/<int:quest_id>", views.quest_details_view.as_view(), name = "view_quest"),
    path('quests/<int:quest_id>/tasks/<int:task_id>', views.task_details_view.as_view(), name = "view_task"),
    path('tasks/<int:task_id>/update', views.update_task, name = 'update_task'),
    path('tasks/<int:task_id>/delete', views.task_delete_view.as_view(), name = "delete_task"),
    path("tasks/<int:task_id>/complete/", views.mark_task_completed, name="mark_task_completed"),
    path('quest/<int:quest_id>/update/', views.update_quest, name='update_quest'),
    path('quest/<int:quest_id>/delete/', views.delete_quest, name='delete_quest'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

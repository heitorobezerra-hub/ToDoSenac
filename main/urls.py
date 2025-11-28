from django.urls import path
from main.views import TaskList, task_concluido, task_pendente, task_create
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', TaskList.as_view(), name='task_list'),
    path('concluidas/', views.task_concluido, name='task_concluido'),
    path('pendente/', views.task_pendente, name='task_pendente'),
    path('create_task', views.task_create, name='create_task'),
    path('update_task/<int:pk>/', views.task_update, name='update_task'),
    path('delete_task/<int:pk>/', views.task_delete, name='delete_task'),
]

from django.urls import path
from main.views import TaskList, task_concluido, task_pendente
from .import views

urlpatterns = [
    path('', TaskList.as_view(), name = 'task_list'),
    path('concluido/', views.task_concluido, name = 'task_concluido'),
    path('pendente/', views.task_pendente, name= 'task_pendente')
]



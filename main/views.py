from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from main.models import Task #Importar tabela que vamos usar
class HomeView(TemplateView):
    template_name = 'home.html' 
    
    
class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'
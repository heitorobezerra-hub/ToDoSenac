from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from main.models import Task #Importar tabela que vamos usar
class HomeView(TemplateView):
    template_name = 'home.html' 
    
    
class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'

def task_concluido(request):
    a = 4
    b = 5
    c = a + b

    tarefas = Task.objects.filter(concluida=1)
    context = {
        "tarefas":tarefas,
        "título_pagina": "Minhas tarefas concluidas",
    }
    return render(request, 'tasks/teste.html', context)

def task_pendente(request):
    a = 4
    b = 5
    c = a + b

    tarefas = Task.objects.filter(concluida=0)
    context = {
        "tarefas":tarefas,
        "título_pagina": "Minhas tarefas concluidas",
    }
    return render(request, 'tasks/teste2.html', context)
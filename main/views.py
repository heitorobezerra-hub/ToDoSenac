from django.shortcuts import render, redirect
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
    return render(request, 'tasks/conclusao.html', context)

def task_pendente(request):
    a = 4
    b = 5
    c = a + b

    tarefas = Task.objects.filter(concluida=0)
    context = {
        "tarefas":tarefas,
        "título_pagina": "Minhas tarefas concluidas",
    }
    return render(request, 'tasks/pendencias.html', context)

def task_create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', "").strip()
        descricao = request.POST.get('descricao', "").strip()
        concluida = request.POST.get('concluida', "") == 'on'
        prioridade = request.POST.get('prioridade', "").strip()
        data_limite = request.POST.get('data_limite', "").strip()
        Task.objects.create(
            titulo=titulo,
            descricao=descricao,
            concluida=concluida,
            prioridade=prioridade,
            data_limite=data_limite
    )
        

    context = {
        'opcoes_prioridade': Task.Priority.choices,
    }
    return render(request, 'tasks/task_form.html', context)


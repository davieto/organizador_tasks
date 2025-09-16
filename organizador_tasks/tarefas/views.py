from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

# LISTAR
def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/index.html', {'tarefas': tarefas})

# CRIAR
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        if titulo:
            Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/create.html')

# EDITAR
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.save()
        return redirect('listar_tarefas')
    return render(request, 'tarefas/edit.html', {'tarefa': tarefa})

# DELETAR
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('listar_tarefas')
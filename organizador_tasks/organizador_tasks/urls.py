from django.contrib import admin
from django.urls import path
from tarefas import views  # importando direto do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('create/', views.criar_tarefa, name='criar_tarefa'),
    path('edit/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('delete/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_membros, name = 'listar_membros'),
    path('view/<int:id>', views.visualizar_membro, name = 'visualizar_membro'),
    path('create/', views.form_membros, name = 'cadastrar_membro'),
    path('edit/<int:id>', views.form_membros, name = 'editar_membro'),
    path('delete/<int:id>/', views.excluir_membro, name='excluir_membro')
]
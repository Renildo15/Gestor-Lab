from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_membros, name = 'listar_membros'),
    path('create/', views.form_membros, name = 'cadastrar_membro'),
    path('<int:id>', views.form_membros, name = 'editar_membro'),
]
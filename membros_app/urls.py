from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_membros, name = 'listar_membros'),
]
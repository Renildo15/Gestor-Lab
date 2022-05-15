from django.urls import path
from . import views

urlpatterns = [
    path('',views.PaginaInicial, name='PaginaInicial'),
]

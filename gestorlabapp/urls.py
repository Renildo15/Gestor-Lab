from django.urls import path
from . import views

urlpatterns = [
    path('',views.pagina_inicial, name='PaginaInicial'),
    path('sobre/', views.sobre, name='sobre'),
]

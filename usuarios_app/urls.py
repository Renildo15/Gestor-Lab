from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.logar_user, name="logar_user"),
    path('cadastro/', views.cadastrar_user, name="cadastrar_user"),
    path('logout/', views.deslogar_usuario, name='deslogar_usuario')
]

from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.logar_user, name="logar_user"),
    path('cadastro/', views.cadastrar_user, name="cadastrar_user"),
    path('logout/', views.deslogar_usuario, name='deslogar_usuario'),
    path('mudar_senha/', views.mudar_senha, name='mudar_senha'),
    path('mudar_senha_sucesso/', views.mudar_senha_sucesso, name='mudar_senha_sucesso'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="senha/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="senha/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="senha/password_reset_complete.html"), name='password_reset_complete'),
]

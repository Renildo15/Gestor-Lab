from django.urls import path
from . import views

app_name ='linhapesquisa'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='linhaForm'),
    path('create/', views.create, name='linhaCreate'),
    path('view/<int:pk>', views.view, name='linhaView'),
    path('edit/<int:pk>', views.edit, name='linhaEdit'),
    path('update/<int:pk>', views.update, name='linhaUpdate'),
    path('delete/<int:pk>', views.delete, name='linhaDelete'),
]
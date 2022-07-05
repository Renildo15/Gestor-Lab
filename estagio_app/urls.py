from os import name
from django.urls import path
from . import views

app_name ='estagio'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='estForm'),
    path('create/', views.create, name='estCreate'),
    path('view/<int:pk>', views.view, name='estView'),
    path('edit/<int:pk>', views.edit, name='estEdit'),
    path('update/<int:pk>', views.update, name='estUpdate'),
    path('delete/<int:pk>', views.delete, name='estDelete'),
]
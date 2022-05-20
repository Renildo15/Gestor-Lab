from os import name
from django.urls import path
from . import views

app_name ='projeto'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='projectForm'),
    path('create/', views.create, name='projectCreate'),
    path('view/<int:pk>', views.view, name='projectView'),
    path('edit/<int:pk>', views.edit, name='projectEdit'),
    path('update/<int:pk>', views.update, name='projectUpdate'),
    path('delete/<int:pk>', views.delete, name='projectDelete'),
] 
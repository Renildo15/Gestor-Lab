from os import name
from django.urls import path
from . import views

app_name ='evento'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='eventForm'),
    path('create/', views.create, name='eventCreate'),
    path('view/<int:pk>', views.view, name='eventView'),
    path('edit/<int:pk>', views.edit, name='eventEdit'),
    path('update/<int:pk>', views.update, name='eventUpdate'),
    path('delete/<int:pk>', views.delete, name='eventDelete'),
]
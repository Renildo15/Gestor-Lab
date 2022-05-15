from os import name
from django.urls import path
from . import views

app_name ='laboratorio'

urlpatterns = [
    path('',views.home, name='home'),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>', views.view, name='view'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]

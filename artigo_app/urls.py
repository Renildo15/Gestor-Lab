from django.urls import path
from . import views

app_name ='artigo'

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='artForm'),
    path('create/', views.create, name='artCreate'),
    path('view/<int:pk>', views.view, name='artView'),
    path('edit/<int:pk>', views.edit, name='artEdit'),
    path('update/<int:pk>', views.update, name='artUpdate'),
    path('delete/<int:pk>', views.delete, name='artDelete'),
]
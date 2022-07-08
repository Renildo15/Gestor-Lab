"""gestorlabproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laboratorio/', include('laboratorio_app.urls')),
    path('evento/', include('evento_app.urls')),
    path('projeto/', include('projetos_app.urls')),
    path('membros/', include('membros_app.urls')),
    path('artigo/', include('artigo_app.urls')),
    path('linhapesquisa/', include('linhapesquisa_app.urls')),
    path('tcc/', include('tcc_app.urls')),
    path('horario/', include('horario_app.urls')),
    path('apresentacao/', include('apresentacao_app.urls')),
    path('estagio/', include('estagio_app.urls')),
    path('auth/', include('usuarios_app.urls')),
    path('', include('gestorlabapp.urls')),
]

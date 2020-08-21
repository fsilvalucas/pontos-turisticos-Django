"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# Django
from django.contrib import admin
from django.urls import path, include

# Django Rest
from rest_framework import routers

# Apps
from pontos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSets
from localizacao.api.viewsets import EnderecoViewSets
from comentarios.api.viewsets import ComentarioViewSets


router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSets)
router.register(r'enderecos', EnderecoViewSets)
router.register(r'comentarios', ComentarioViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]

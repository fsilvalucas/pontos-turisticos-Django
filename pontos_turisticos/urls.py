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
from pontos.api.viewsets import PontosTuristicosViewSet
from atracoes.api.viewsets import AtracoesViewSets
from localizacao.api.viewsets import EnderecoViewSets


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontosTuristicosViewSet)
router.register(r'atracao', AtracoesViewSets)
router.register(r'endereco', EnderecoViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]

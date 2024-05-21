"""
URL configuration for miapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_estudiante/', views.agregar_estudiante, name='agregar_estudiante'),
    path('agregar_entregable/', views.agregar_entregable, name='agregar_entregable'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
    path('', views.buscar_curso, name='buscar_curso'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'), 
]

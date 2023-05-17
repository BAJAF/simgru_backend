"""simgruBackend URL Configuration

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
from django.urls import include, path

from simgru import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('jwt/<str:token>/', views.jwt_view, name='jwt'),
    path('courses/<str:jwt>/', views.courses_view, name='courses'),
    path('atributos/', views.get_aes, name="aes"),
    path('atributos/<int:ae_id>/', views.get_ae_crits, name="crits"),
    path('atributos/<int:ae_id>/criterios/<int:crit_id>/', views.get_ae_crit_inds, name="inds"),
    path('code/ae/<int:ae>/cd/<int:cd>/i/<int:i>/', views.create_code, name='code'),
    path('courses/<str:courseId>/coursework/<str:courseworkId>/', views.get_coursework_info, name='coursework')
    # Por si es necesario de manera POST
    # path('jwt/', views.jwt_view, name='jwt'),
]

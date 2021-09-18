"""project1604 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.sign_up),
    path('', views.login, name ='login'),
    path('sign_up', views.sign_up, name ='sign_up'),
    path('sdn_dashboard1', views.sdn_dashboard1, name ='sdn_dashboard1'),
    #path('sdn_dashboard1', views.sdn_dashboard1, name ='sdn_dashboard1'),
    #path('myapp.views', url('', views.login, name ='login'), url('sdn_dashboard1', views.sdn_dashboard1, name ='sdn_dashboard1'))
    ]

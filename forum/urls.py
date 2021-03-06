"""config URL Configuration

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
from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:presenting_id>/', views.detail, name='detail'),
    path('suggestion/create/<int:presenting_id>/', views.suggestion_create, name='suggestion_create'),
    path('presenting/create/', views.presenting_create, name='presenting_create'),
    path('presenting/modify/<int:presenting_id>/', views.presenting_modify, name='presenting_modify'),
    path('presenting/delete/<int:presenting_id>/', views.presenting_delete, name='presenting_delete'),
]
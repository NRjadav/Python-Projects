"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('change_password/', views.change_password,name='change_password'),
    path('update_profile/', views.update_profile,name='update_profile'),
    path('add_student/', views.add_student,name='add_student'),
    path('all_students/', views.all_students,name='all_students'),
    path('add_teacher/', views.add_teacher,name='add_teacher'),
    path('all_teachers/', views.all_teachers,name='all_teachers'),
    path('time_table/', views.time_table,name='time_table'),
    path('evants_photo/', views.evants_photo,name='evants_photo'),







]

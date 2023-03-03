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
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('change_password',views.change_password,name='change_password'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('add_member',views.add_member,name='add_member'),
    path('all_members',views.all_members,name='all_members'),
    path('image',views.image,name='image'),
    path('add_notice',views.add_notice,name='add_notice'),
    path('sell_home',views.sell_home,name='sell_home'),
    path('buy_home',views.buy_home,name='buy_home'),

]

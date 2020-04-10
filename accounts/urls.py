#coding=utf-8
'''
Created on 2020��3��13��

@author: zcy
'''
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]
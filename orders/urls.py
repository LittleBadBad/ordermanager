#coding=utf-8
from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.index, name='index'),
    path('neworder', views.order, name='neworder'),
    path('save/<orderid>', views.save, name='save'),
    path('delete/', views.delete, name='delete'),
    path('edit/<orderid>', views.edit, name='edit'),
    path('submit/', views.submit, name='submit'),
    path('verify/<orderid>', views.checkorder, name='verify'),
    path('pass/', views.passorder, name='pass'),
    path('reject/<orderid>', views.reject, name='reject'),
    path('publish/<orderid>', views.checkorder, name='publish'),
    path('publishorder/', views.publishorder, name='publishorder'),
] 
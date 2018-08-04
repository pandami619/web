from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import ListView, DetailView
from order import views

urlpatterns = [
    url(r'^backet_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]
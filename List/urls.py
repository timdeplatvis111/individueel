from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:soundtrackid>/', views.detail, name='detail'),
]
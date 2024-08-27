from django.contrib import admin
from django.urls import path, include
from boot.views import index

urlpatterns = [
    path('', index),
]
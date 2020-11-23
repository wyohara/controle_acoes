from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('success', success_action, name="success_save")
]

from django.contrib import admin
from django.urls import path,include
from bus import views

urlpatterns = [
    path('',views.fun1)
]
from django.urls import path
from . import views
# from django.shortcuts import render


urlpatterns = [
    path('',views.login_view,name='login'),
    path('abc/',views.homepage2,name='list'),
    path('success/', views.success_view, name='success'),

]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate/', views.calculate_profit, name='calculate_profit'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cargar-excel/', views.cargar_consumos, name='cargar_excel'),
    path('dashboard/', views.dashboard_gemini, name='dashboard'),
]
from django.urls import path
from . import views

urlpatterns = [
    # 1. LA PORTADA BONITA (Ahora se llama 'inicio' en views.py)
    path('', views.inicio, name='inicio'),

    # 2. EL PANEL DE DATOS (Antes era 'home', ahora es 'dashboard')
    path('dashboard/', views.dashboard, name='dashboard'),

    # 3. LAS OTRAS RUTAS (Se mantienen igual)
    path('registrar/', views.registrar_consumo, name='registrar_consumo'),
    path('cargar-excel/', views.cargar_consumos, name='cargar_excel'),
]
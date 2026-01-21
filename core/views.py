import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PerfilUsuario, RegistroConsumo
# Asegúrate de importar tu función de Gemini si la creaste en utils.py
# from .utils import generar_recomendacion_gemini 

def home(request):
    return render(request, 'home.html')

def cargar_consumos(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        excel_file = request.FILES['archivo']
        try:
            # Leemos el Excel con Pandas
            df = pd.read_excel(excel_file)
            
            # Iteramos fila por fila (asumiendo columnas: cedula, tipo, cantidad)
            for index, row in df.iterrows():
                # Buscamos o creamos el usuario
                usuario, created = PerfilUsuario.objects.get_or_create(
                    cedula=str(row['cedula']),
                    defaults={'nombres': 'Usuario Importado', 'email': f"user{row['cedula']}@test.com"}
                )
                
                # Guardamos el consumo
                RegistroConsumo.objects.create(
                    usuario=usuario,
                    tipo_recurso=row['tipo'], # ej: luz, agua
                    cantidad=row['cantidad']
                )
            
            messages.success(request, f'Se cargaron {len(df)} registros exitosamente.')
            return redirect('dashboard')
            
        except Exception as e:
            messages.error(request, f"Error al procesar el archivo: {e}")
            
    return render(request, 'cargar_excel.html')

def dashboard_gemini(request):
    # Aquí mostraremos los datos y la IA
    consumos = RegistroConsumo.objects.all().order_by('-fecha_consumo')[:10]
    return render(request, 'dashboard.html', {'consumos': consumos})
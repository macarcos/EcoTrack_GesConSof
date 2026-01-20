from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.shortcuts import render
from .models import PerfilUsuario, RegistroConsumo

def cargar_excel(request):
    if request.method == 'POST' and request.FILES['archivo']:
        df = pd.read_excel(request.FILES['archivo'])
        for _, row in df.iterrows():
            # Busca al usuario por la cédula que ya definiste en tu modelo
            usuario, _ = PerfilUsuario.objects.get_or_create(cedula=row['cedula'])
            RegistroConsumo.objects.create(
                usuario=usuario,
                tipo_recurso=row['tipo'],
                cantidad=row['cantidad']
            )
        return render(request, 'exito.html')
    return render(request, 'cargar.html')
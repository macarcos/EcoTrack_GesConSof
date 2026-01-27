import google.generativeai as genai
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum, Q
import pandas as pd
import json
from .models import PerfilUsuario, RegistroConsumo
from .forms import ConsumoForm

# --- CONFIGURACIÓN GEMINI ---
GOOGLE_API_KEY = "AIzaSyA3OPO_KMd7T8PUMq3vMlgXlMSJukAOOWU" # <--- ¡VERIFICA QUE ESTÉ TU CLAVE!
genai.configure(api_key=GOOGLE_API_KEY)

# Conexión Inteligente
model = None
try:
    print("--- 📡 Buscando modelo Gemini... ---")
    lista_modelos = genai.list_models()
    modelos_disponibles = [m.name for m in lista_modelos if 'generateContent' in m.supported_generation_methods]
    if modelos_disponibles:
        nombre_modelo = next((m for m in modelos_disponibles if 'flash' in m), modelos_disponibles[0])
        model = genai.GenerativeModel(nombre_modelo)
        print(f"✅ IA CONECTADA: {nombre_modelo}")
    else:
        print("⚠️ No hay modelos disponibles.")
except Exception as e:
    print(f"❌ Error Gemini: {e}")

# --- FUNCIONES IA ---
def obtener_consejo_individual(usuario, recurso, cantidad, historial):
    if not model: return "Análisis no disponible temporalmente."
    try:
        prompt = (
            f"Usuario: {usuario}. Recurso: {recurso}. Consumo actual: {cantidad}. "
            f"Historial previo: {historial}. "
            "Actúa como un experto en sostenibilidad. "
            "Si el consumo subió, dame 1 consejo práctico y corto. "
            "Si bajó, felicítalo."
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return "No se pudo generar el consejo."

def obtener_resumen_lote(lista_datos):
    if not model: return "Análisis no disponible."
    try:
        datos_texto = "\n".join(lista_datos[:80])
        prompt = (
            f"Datos:\n{datos_texto}\n"
            "Dame un resumen estratégico breve en HTML simple (sin ```html):\n"
            "<b>Graves:</b> Quién gastó más y cuánto.\n"
            "<b>Leves:</b> Quién gastó menos.\n"
            "<b>Acción:</b> Una recomendación general."
        )
        response = model.generate_content(prompt)
        return response.text.replace("```html", "").replace("```", "")
    except Exception:
        return "Error en resumen."

# --- VISTAS ---

def inicio(request):
    return render(request, 'inicio.html')

def dashboard(request):
    # Filtros
    busqueda = request.GET.get('q')
    fecha_filtro = request.GET.get('fecha')
    
    consumos = RegistroConsumo.objects.all().order_by('-fecha_consumo')

    if busqueda:
        consumos = consumos.filter(Q(usuario__nombres__icontains=busqueda) | Q(usuario__cedula__icontains=busqueda))
    if fecha_filtro:
        consumos = consumos.filter(fecha_consumo=fecha_filtro)

    # Gráfico
    datos_grafico = RegistroConsumo.objects.values('tipo_recurso').annotate(total=Sum('cantidad'))
    labels = [x['tipo_recurso'].upper() for x in datos_grafico]
    data = [x['total'] for x in datos_grafico]

    # Tabla con comparación
    datos_procesados = []
    for c in consumos[:50]: # Límite para velocidad
        anterior = RegistroConsumo.objects.filter(
            usuario=c.usuario, tipo_recurso=c.tipo_recurso, fecha_consumo__lt=c.fecha_consumo
        ).order_by('-fecha_consumo').first()
        
        es_mayor = c.cantidad > anterior.cantidad if anterior else False
        datos_procesados.append({'obj': c, 'es_mayor': es_mayor})

    context = {
        'consumos': datos_procesados,
        'labels_grafico': json.dumps(labels),
        'data_grafico': json.dumps(data)
    }
    return render(request, 'home.html', context)

def registrar_consumo(request):
    if request.method == 'POST':
        form = ConsumoForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula_usuario']
            nombres = form.cleaned_data['nombre_usuario']
            consumo = form.save(commit=False)
            
            usuario, _ = PerfilUsuario.objects.get_or_create(
                cedula=cedula, defaults={'nombres': nombres, 'email': f"{cedula}@test.com"}
            )
            
            # --- VALIDACIÓN DE DUPLICADOS MEJORADA ---
            existe = RegistroConsumo.objects.filter(
                usuario=usuario, 
                tipo_recurso=consumo.tipo_recurso, 
                fecha_consumo=consumo.fecha_consumo
            ).exists()
            
            if existe:
                # MENSAJE DE ERROR PERSONALIZADO
                messages.error(request, f"⛔ ALTO: {nombres} ya registró '{consumo.tipo_recurso}' en la fecha {consumo.fecha_consumo}. Intenta con otra fecha.")
                return redirect('registrar_consumo')
            
            # Si pasa, seguimos con la IA
            consumo.usuario = usuario
            historial = list(RegistroConsumo.objects.filter(
                usuario=usuario, tipo_recurso=consumo.tipo_recurso
            ).values_list('cantidad', flat=True).order_by('-fecha_consumo')[:3])
            
            consumo.recomendacion_ia = obtener_consejo_individual(nombres, consumo.tipo_recurso, consumo.cantidad, historial)
            consumo.save()
            
            messages.success(request, '✅ Consumo guardado correctamente.')
            return redirect('dashboard') # <--- AQUÍ ESTABA EL ERROR (antes decía 'home')
    else:
        form = ConsumoForm()
    return render(request, 'registrar_consumo.html', {'form': form})

def cargar_consumos(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        try:
            df = pd.read_excel(request.FILES['archivo'])
            guardados = 0
            omitidos = 0
            datos_ia = []

            for _, row in df.iterrows():
                cedula = str(row['cedula'])
                fecha = pd.to_datetime(row.get('fecha', timezone.now().date())).date()
                nombre = row.get('nombres', 'Usuario Excel')
                
                usuario, _ = PerfilUsuario.objects.get_or_create(
                    cedula=cedula, defaults={'nombres': nombre, 'email': f"u{cedula}@test.com"}
                )

                if RegistroConsumo.objects.filter(usuario=usuario, tipo_recurso=row['tipo'], fecha_consumo=fecha).exists():
                    omitidos += 1
                else:
                    RegistroConsumo.objects.create(
                        usuario=usuario, tipo_recurso=row['tipo'], cantidad=row['cantidad'], fecha_consumo=fecha
                    )
                    guardados += 1
                    datos_ia.append(f"{nombre} ({row['tipo']}): {row['cantidad']}")

            if guardados > 0:
                analisis = obtener_resumen_lote(datos_ia)
                messages.success(request, f"Cargados: {guardados}. Repetidos omitidos: {omitidos}")
                messages.info(request, analisis) # La IA manda el resumen aquí
            else:
                messages.warning(request, f"No se cargaron nuevos datos. {omitidos} repetidos.")
                
            return redirect('dashboard') # <--- CORREGIDO TAMBIÉN AQUÍ

        except Exception as e:
            messages.error(request, f"Error archivo: {e}")
            
    return render(request, 'cargar_excel.html')
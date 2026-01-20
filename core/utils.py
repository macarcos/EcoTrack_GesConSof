import google.generativeai as genai
from .models import RegistroConsumo

def generar_recomendacion_gemini(registro_id):
    # Configuración de la IA
    genai.configure(api_key="TU_API_KEY_AQUI")
    model = genai.GenerativeModel('gemini-pro')
    
    # Obtener los datos desde Postgres
    registro = RegistroConsumo.objects.get(id=registro_id)
    
    prompt = (f"Actúa como un experto ambiental. El usuario {registro.usuario.nombres} "
              f"registró un consumo de {registro.cantidad} en el recurso {registro.tipo_recurso}. "
              f"Dame una recomendación técnica y breve para reducir este consumo.")

    try:
        response = model.generate_content(prompt)
        # Guardamos la respuesta en el campo que ya tienes en tu modelo
        registro.recomendacion_ia = response.text
        registro.save()
        return True
    except Exception as e:
        print(f"Error con Gemini: {e}")
        return False
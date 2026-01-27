import google.generativeai as genai

# --- PEGA TU CLAVE AQUÍ ---
GOOGLE_API_KEY = "AIzaSyA3OPO_KMd7T8PUMq3vMlgXlMSJukAOOWU" 
genai.configure(api_key=GOOGLE_API_KEY)

print("📡 Conectando con Google para ver modelos disponibles...")

try:
    # Listamos los modelos que sirven para generar texto
    hay_modelos = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ MODELO DISPONIBLE: {m.name}")
            hay_modelos = True
    
    if not hay_modelos:
        print("⚠️ No se encontraron modelos. Verifica si tu API Key tiene permisos.")

except Exception as e:
    print(f"❌ Error grave: {e}")
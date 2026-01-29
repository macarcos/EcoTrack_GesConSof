# GUÍA DE INSTALACIÓN: EcoTrack (Paso a Paso)
# Esta guía explica cómo instalar el proyecto desde cero # en una computadora nueva (ej. Laboratorio de la Universidad).

# PASO 1: Descargar las Herramientas (Links Oficiales)
# Instala estos programas en este orden.

# "Git (Para bajar el código):

https://git-scm.com/install/windows

# Instalación: Dale "Siguiente" a todo.

# Python 3.10.11 (Opcional si usas Docker, pero # recomendado tenerlo):

https://www.python.org/downloads/release/python-31011/

# OJO: Al abrir el instalador, marca la casilla "Add Python 3.10 to PATH" antes de instalar.

# Docker Desktop (El motor del proyecto):

https://www.docker.com/products/docker-desktop/

# Instalación: Instala y reinicia la computadora.

# PASO 2: Preparar Docker (¡Truco para PC de Universidad!)
# Las computadoras de universidad suelen tener el sistema desactualizado. Antes de arrancar, haz esto para evitar errores:
# Abre una terminal (PowerShell o CMD).
# Escribe:
# PowerShell

wsl --update

# Abre Docker Desktop y espera a que la barra de abajo a la izquierda esté en VERDE.

# PASO 3: Arrancar el Proyecto
# Bajar el código: Abre una terminal en el Escritorio y escribe:

# PowerShell

git clone https://github.com/macarcos/EcoTrack_GesConSof.git
cd EcoTrack_GesConSof

# Encender el Servidor (Comando Mágico): Este comando instala TODO automáticamente (Django, Pandas, openpyxl para Excel, la API de Gemini, etc).

# PowerShell

docker-compose up --build

# Espera a que termine de descargar y aparezca: Listening at: http://0.0.0.0:8000.
# Nota sobre openpyxl: No necesitas instalarlo manual. Docker lo instala solo porque está en las dependencias del proyecto.
# PASO 4: Crear Administrador (Base de Datos Nueva)
# Como es una PC nueva, no tienes usuario. Crea uno rápido:
# No cierres la terminal anterior. Abre una NUEVA terminal en VS Code (+).
# Escribe:
# PowerShell

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
# -----------------Crea tu usuario (ej: Marcos / Admin123).

# PASO 5: ¡Presentar!
# Abre tu navegador (Chrome/Edge):

👉 Tu Sistema Web: http://127.0.0.1:8000/

👉 Panel Admin: http://127.0.0.1:8000/admin/
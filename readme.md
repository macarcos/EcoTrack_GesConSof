Microsoft Windows [Versión 10.0.26200.7623]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Windows\System32>mkdir EcoTrack_GesConSof

C:\Windows\System32>cd EcoTrack_GesConSof

C:\Windows\System32\EcoTrack_GesConSof>git init
Initialized empty Git repository in C:/Windows/System32/EcoTrack_GesConSof/.git/

C:\Windows\System32\EcoTrack_GesConSof>python -m venv venv

C:\Windows\System32\EcoTrack_GesConSof>pip install django
Collecting django
  Downloading django-6.0.1-py3-none-any.whl.metadata (3.9 kB)
Collecting asgiref>=3.9.1 (from django)
  Downloading asgiref-3.11.0-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.5.0 (from django)
  Downloading sqlparse-0.5.5-py3-none-any.whl.metadata (4.7 kB)
Requirement already satisfied: tzdata in c:\users\det-pc\appdata\roaming\python\python313\site-packages (from django) (2025.2)
Downloading django-6.0.1-py3-none-any.whl (8.3 MB)
   ---------------------------------------- 8.3/8.3 MB 1.2 MB/s  0:00:07
Downloading asgiref-3.11.0-py3-none-any.whl (24 kB)
Downloading sqlparse-0.5.5-py3-none-any.whl (46 kB)
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.11.0 django-6.0.1 sqlparse-0.5.5

C:\Windows\System32\EcoTrack_GesConSof>django-admin startproject config .

C:\Windows\System32\EcoTrack_GesConSof>python manage.py startapp core

C:\Windows\System32\EcoTrack_GesConSof>venv/
"venv" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Windows\System32\EcoTrack_GesConSof>__pycache__/
"__pycache__" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Windows\System32\EcoTrack_GesConSof>*.pyc
"*.pyc" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Windows\System32\EcoTrack_GesConSof>db.sqlite3
"db.sqlite3" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Windows\System32\EcoTrack_GesConSof>(echo venv/ && echo __pycache__/ && echo *.pyc && echo db.sqlite3) > .gitignore

C:\Windows\System32\EcoTrack_GesConSof>venv\Scripts\activate

(venv) C:\Windows\System32\EcoTrack_GesConSof>pip install django
Collecting django
  Using cached django-6.0.1-py3-none-any.whl.metadata (3.9 kB)
Collecting asgiref>=3.9.1 (from django)
  Using cached asgiref-3.11.0-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.5.0 (from django)
  Using cached sqlparse-0.5.5-py3-none-any.whl.metadata (4.7 kB)
Collecting tzdata (from django)
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached django-6.0.1-py3-none-any.whl (8.3 MB)
Using cached asgiref-3.11.0-py3-none-any.whl (24 kB)
Using cached sqlparse-0.5.5-py3-none-any.whl (46 kB)
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.11.0 django-6.0.1 sqlparse-0.5.5 tzdata-2025.3

[notice] A new release of pip is available: 25.2 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) C:\Windows\System32\EcoTrack_GesConSof>git add .

(venv) C:\Windows\System32\EcoTrack_GesConSof>git commit -m "Inicialización del proyecto EcoTrack: Estructura base"
[master (root-commit) b9468d7] Inicialización del proyecto EcoTrack: Estructura base
 14 files changed, 214 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 config/__init__.py
 create mode 100644 config/asgi.py
 create mode 100644 config/settings.py
 create mode 100644 config/urls.py
 create mode 100644 config/wsgi.py
 create mode 100644 core/__init__.py
 create mode 100644 core/admin.py
 create mode 100644 core/apps.py
 create mode 100644 core/migrations/__init__.py
 create mode 100644 core/models.py
 create mode 100644 core/tests.py
 create mode 100644 core/views.py
 create mode 100644 manage.py

(venv) C:\Windows\System32\EcoTrack_GesConSof>git checkout -b develop
Switched to a new branch 'develop'

(venv) C:\Windows\System32\EcoTrack_GesConSof>python manage.py makemigrations
No changes detected

(venv) C:\Windows\System32\EcoTrack_GesConSof>python manage.py makemigrations
Migrations for 'core':
  core\migrations\0001_initial.py
    + Create model PerfilUsuario
    + Create model RegistroConsumo

(venv) C:\Windows\System32\EcoTrack_GesConSof>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying core.0001_initial... OK
  Applying sessions.0001_initial... OK

(venv) C:\Windows\System32\EcoTrack_GesConSof>git add .

(venv) C:\Windows\System32\EcoTrack_GesConSof>git commit -m "Feat: Creación de esquemas de base de datos (Modelos)"
[develop d24b55b] Feat: Creación de esquemas de base de datos (Modelos)
 3 files changed, 71 insertions(+), 1 deletion(-)
 create mode 100644 core/migrations/0001_initial.py

(venv) C:\Windows\System32\EcoTrack_GesConSof>move "C:\Windows\System32\EcoTrack_GesConSof" "%USERPROFILE%\Desktop\"
El proceso no tiene acceso al archivo porque está siendo utilizado por otro proceso.

(venv) C:\Windows\System32\EcoTrack_GesConSof>cd \

(venv) C:\>cd \

(venv) C:\>move "C:\Windows\System32\EcoTrack_GesConSof" "%USERPROFILE%\Desktop\"
Se ha(n) movido         1 directorio(s).

(venv) C:\>cd /d "%USERPROFILE%\Desktop\EcoTrack_GesConSof"

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>type nul > Dockerfile

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>type nul > docker-compose.yml

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>type nul > requirements.txt

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>code .

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>docker-compose up --build
"docker-compose" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>docker compose up --build
"docker" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

(venv) C:\Users\Det-Pc\Desktop\EcoTrack_GesConSof>

## Proyecto Finalizad

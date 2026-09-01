# Gestor de Proyectos y Tareas en Django

Aplicación web desarrollada con Django y Bootstrap para la gestión de proyectos y tareas individuales, con autenticación de usuarios y aislamiento de datos por cuenta.

---

## Características
* **Autenticación:** Registro, inicio y cierre de sesión de usuarios.
* **Proyectos:** Crear, listar, ver detalles, editar y eliminar proyectos propios.
* **Tareas:** Añadir tareas a un proyecto, alternar estado (*completada/pendiente*) y eliminar.
* **Seguridad:** Aislamiento de registros a nivel de usuario (`request.user`).

---

## Instalación y Configuración

Sigue estos pasos en tu terminal para ejecutar el proyecto localmente:

1. Clonar el repositorio y entrar al directorio

git clone [https://github.com/Al-Sagredo/Django_web_app](https://github.com/Al-Sagredo/Django_web_app)  
cd proyecto_django  

 2. Crear y activar el entorno virtual  
 python -m venv venv  
venv\Scripts\activate  

3. Instalar dependencias  
pip install django  

4. Aplicar migraciones  
python manage.py makemigrations  
python manage.py migrate  

5. Crear un superusuario (Opcional)  
python manage.py createsuperuser      

6. Iniciar el servidor de desarrollo  
python manage.py runserver  

Listo! Ingresa a http://127.0.0.1:8000/ en tu navegador.  

Estructura del Proyecto  
├── core/                       # Aplicación principal
│   ├── migrations/             # Migraciones de base de datos
│   ├── templates/core/         # Plantillas de la app (proyecto_list, detalle, forms)
│   ├── admin.py                # Configuración de Django Admin
│   ├── forms.py                # ProyectoForm y TareaForm
│   ├── models.py               # Modelos Proyecto y Tarea
│   ├── urls.py                 # Enrutamiento de la app
│   └── views.py                # Lógica y controladores (FBV / CBV)
├── templates/                  # Plantillas globales (base.html, home.html, login, registro)
├── proyecto_gestor/            # Configuración global del proyecto
│   ├── settings.py             # Ajustes y configuración general
│   ├── urls.py                 # URLs principales
│   └── wsgi.py
├── db.sqlite3                  # Base de datos SQLite
├── manage.py                   # Script de gestión de Django
└── README.md

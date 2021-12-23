# Informatorio 2021 - Comision 5

Curso Informatorio Cenit Subsecretaría de Empleo de la Provincia del Chaco
Profesor: Blas Cabas

Integrantes:
  * Alejandro Funes
  * Mariano Cendra

Proyecto: Blog (Tema: Los 17 Objetivos de Desarrollo Sostenible)

# Sistema

- Windows 10 Pro version 21H1
- Python 3.10.x
- Django 3.1

# Instalacion

Dependencias:

  - celery = 5.2.1
  - Django = 3.1
  - Pillow = 8.4.0
  - django-crispy-forms = 1.13.0
  - django-storages = 1.12.3
  - django-tinymce = 3.4.0
  
  Instalacion automatica de dependencias
  
    pip install -r requirements.txt
  
  Instalacion manual de dependencias
  
    pip install Django==3.1
    pip install django-crispy-forms
    pip install django-storages
    pip install django-tinymce
    pip install Pillow
    pip install celery

# Uso

Si las dependencias estan correctas no hace falta migrar cambios a la base de datos.

Ejecutar:
 python manage.py runserver 127.0.0.1:8000

 Datos de acceso:
 
 - Cuenta Propietario contraseña informatorio (Perfil de superusuario)
 - Cuenta Mariano contraseña informatorio (Perfil de Blog Admin)
 - Cuenta Alejandro contraseña informatorio (Perfil de Writer)
 - Cuenta Usuario contraseña informatorio (Perfil de Reader)

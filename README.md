# Plataforma de Estudio

¡Bienvenido a nuestra plataforma de estudio! Este proyecto consiste en una aplicación web para gestionar cursos, profesores, alumnos y entregas.

## Uso de la Plataforma

Para poder ejecutar este proyecto en tu entorno local, necesitas tener instalados los siguientes programas:

- Visual Studio Code (https://code.visualstudio.com/)
- Python (https://www.python.org/downloads/)
- Django (puedes instalarlo mediante pip: `pip install django`)

## Testear el Servidor

Una vez que tengas instaladas las herramientas necesarias, puedes iniciar el servidor Django utilizando el siguiente comando en tu terminal dentro del directorio del proyecto:

python manage.py runserver
### Acceso a la Plataforma

Para acceder a la plataforma, [visita nuestra página principal](http://127.0.0.1:8000/).

### Acceso al Panel de Administración

Utiliza el [Panel de Administración](http://127.0.0.1:8000/admin/miapp/curso/) para gestionar los datos de la aplicación.

- **Usuario:** admin
- **Contraseña:** admin123

## Funcionalidades

1. **Página Principal**
   - [Busca cursos por camada](http://127.0.0.1:8000/).

2. **Menú de Opciones**
   - **Agregar Profesores**
     - Añade profesores con nombre, apellido, correo electrónico y profesión.
   - **Agregar Cursos**
     - Añade cursos con nombre y camada.
   - **Agregar Alumnos**
     - Añade alumnos con nombre, apellido y correo electrónico.
   - **Agregar Entregas**
     - Añade una entrega con nombre, fecha de entrega y estado (entregado o pendiente).


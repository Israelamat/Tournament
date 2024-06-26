# Tournament - Plataforma de Gestión de Ligas

## Descripción
Tournament es una plataforma web desarrollada con Python y Django que facilita la gestión de ligas deportivas con múltiples torneos. Proporciona herramientas para la creación de ligas, la administración de equipos, la programación de partidos y más.

## Características

- **Gestión de Ligas:** Crear, editar y eliminar ligas deportivas.
- **Configuración de Torneos:** Definir múltiples torneos dentro de una liga.
- **Administración de Equipos:** Agregar, modificar y retirar equipos de los torneos.
- **Programación de Partidos:** Crear y gestionar calendarios de partidos.
- **Seguimiento de Estadísticas:** Registrar y visualizar estadísticas de jugadores y equipos.
- **Interfaz Responsiva:** Diseño adaptable para una experiencia de usuario óptima en diferentes dispositivos.

## Requisitos del Sistema

- Python 3.9.5
- Django 4.2.9
- Navegador web moderno

## Instalación

1. Clona el repositorio: `https://github.com/Israelamat/Tournament.git`
2. Crea y activa un entorno virtual: `python -m venv venv` y `source venv/bin/activate` (en sistemas Unix) o `venv\Scripts\activate` (en Windows).
3. Instala las dependencias: `pip install -r requirements.txt`
4. Aplica las migraciones: `python manage.py migrate`
5. Inicia el servidor de desarrollo: `python manage.py runserver`
6. El servidor de pruebas se iniciará y mostrará un mensaje indicando en qué dirección IP y puerto está escuchando. Por lo general, será algo como `Starting development server at http://127.0.0.1:8000/`.
7. Abre tu navegador web y ve a la dirección `http://127.0.0.1:8000/` (o la dirección IP y puerto que se mostró en el paso anterior). Verás la página de inicio de tu proyecto Django si todo está configurado correctamente.****

## Capturas de Pantalla
![Captura de Pantalla 1](https://i.postimg.cc/qRdVs0gD/home.png) | [![login.png](https://i.postimg.cc/zBSmpMgz/login.png)](https://postimg.cc/2b6XS0GM) | [![tourn2.png](https://i.postimg.cc/3NRJWNpJ/tourn2.png)](https://postimg.cc/7GFyWxmp) | [![tourn3-PNG.png](https://i.postimg.cc/rwhcbMtS/tourn3-PNG.png)](https://postimg.cc/5XFZQcg0)

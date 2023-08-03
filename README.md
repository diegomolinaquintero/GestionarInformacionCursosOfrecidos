# GestionarInformacionCursosOfrecidos

## Descripción

Necesitamos desarrollar una aplicación web para gestionar la información de los cursos ofrecidos por Cesde. La aplicación debe permitir a los administradores agregar, editar y eliminar cursos, así como también mostrar una lista de todos los cursos disponibles. Igualmente, la aplicación debe permitir administrar los docentes que dictarán cada curso.

## Bienvenido a GestionApp

Esta es la página de inicio de la aplicación GestionApp.

## Proyecto de Aplicación Web para Gestión de Cursos - Documentación

Este repositorio contiene una aplicación web desarrollada en Django para gestionar la información de los cursos ofrecidos por Cesde. La aplicación permite a los administradores agregar, editar y eliminar cursos, así como también mostrar una lista de todos los cursos disponibles. Además, la aplicación permite administrar los docentes que dictarán cada curso.

### Instalación de Django

Para ejecutar este proyecto, es necesario tener Python y Django instalados en su sistema. Si aún no tiene Django instalado, puede seguir los siguientes pasos:

1. Asegúrese de tener Python instalado en su sistema. Puede descargar Python desde el sitio oficial: [Descargar Python](https://www.python.org/downloads/)
1. Abra una ventana de terminal y ejecute el siguiente comando para instalar Django:

```bash

pip install django

Una vez instalado Django, puede verificar que se haya instalado correctamente ejecutando:



django-admin --version

Configuración de la Base de Datos

Este proyecto utiliza SQLite como base de datos predeterminada. Sin embargo, también es posible utilizar PostgreSQL si así se prefiere. A continuación, se proporcionan instrucciones para ambas opciones:

SQLite (predeterminado)

No es necesario realizar ninguna configuración adicional para usar SQLite, ya que es la base de datos predeterminada de Django. La configuración se encuentra en el archivo settings.py en la carpeta del proyecto.

PostgreSQL

Si desea utilizar PostgreSQL en lugar de SQLite, siga estos pasos:

Asegúrese de tener PostgreSQL instalado en su sistema y cree una base de datos para el proyecto.

En el archivo settings.py en la carpeta del proyecto, busque la sección DATABASES y configure los parámetros de conexión de la siguiente manera:



DATABASES = {

'default': {

'ENGINE': 'django.db.backends.postgresql',

'NAME': 'nombre_de_su_base_de_datos',

'USER': 'su_usuario',

'PASSWORD': 'su_contraseña',

'HOST': 'localhost',

'PORT': '5432',  # Puerto predeterminado de PostgreSQL

}

}

Asegúrese de instalar el adaptador PostgreSQL para Django ejecutando:



pip install psycopg2-binary

Ejecución del Proyecto

Una vez que haya configurado la base de datos según su preferencia, puede seguir estos pasos para ejecutar el proyecto:

Clone o descargue este repositorio en su sistema.

Abra una ventana de terminal y navegue hasta la carpeta del proyecto.

Ejecute el siguiente comando para instalar los requerimientos (se recomienda crear un entorno virtual):



pip install -r requirements.txt

Ejecute el siguiente comando para aplicar las migraciones y crear las tablas en la base de datos:



python manage.py migrate

Inicie el servidor de desarrollo de Django ejecutando:



python manage.py runserver

Abra su navegador web y vaya a la dirección http://127.0.0.1:8000/ para acceder a la aplicación.

Uso de la Aplicación

Una vez que la aplicación esté en funcionamiento, podrá agregar, editar y eliminar cursos, así como administrar los docentes que dictarán cada curso. La interfaz es intuitiva y seguirá las instrucciones en pantalla.

Notas Finales

Este proyecto es una implementación básica de la aplicación web solicitada. Puede ser extendido y mejorado para cumplir con requisitos adicionales y características avanzadas.

Si decide utilizar PostgreSQL en lugar de SQLite, asegúrese de que PostgreSQL esté correctamente configurado en su sistema.

¡Gracias por revisar esta documentación! Si tiene alguna pregunta o necesita ayuda adicional, no dude en ponerse en contacto.


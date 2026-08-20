# Django Rest Framework 2026

Proyecto para las clases virtuales sincrónicas del Instituto Tecnológico Río Cuarto (ITEC) para el espacio curricular "Ingeniería de Software"

- [Clonar el Repo](#clonar-el-repo)
- [Comandos para crear un nuevo proyecto](#crear-proyecto-nuevo-con-uv)
- [Comandos rápidos](#comandos-rápidos)
- [Estructura del proyecto](#estructura-básica-del-proyecto)


## Clonar el repo

Si te querés traer este mismo repo, tenés que:

### 1. Clonar el repositorio con ssh

```shell
git clone git@github.com:FacuLemo/drf-2026.git
```

### 2. Entrar en el proyecto
```shell
cd drf-2026
```

### 3. Instalar las dependencias

Como el proyecto utiliza uv, podés instalar las dependencias definidas en el proyecto con:
```shell
uv sync
```
Esto creará/actualizará el entorno virtual y sincronizará las dependencias del proyecto.
Si no tienen uv, lo encuentran [acá](#crear-proyecto-nuevo-con-uv)


### 4. Ejecutar las migraciones

Entra en src:
```shell
cd src
```

Y ejecuta:
```shell
uv run manage.py migrate
```

### 5. Ahora se inicia el servidor con:
```shell
uv run manage.py runserver
```

El proyecto estará disponible normalmente en:
```shell
http://127.0.0.1:8000/
```

# Crear Proyecto nuevo con uv

### 1. Instalar uv

Si todavía no tienes uv, puedes instalarlo ejecutando:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Si no funciona consulten la [documentación oficial](https://astral.sh/uv)

Después, reinicia la terminal para que uv quede disponible en el PATH.

### 2. Crear el proyecto

Inicializa un nuevo proyecto con:
```shell
uv init Proyecto-django
```

Entra en la carpeta:
```shell
cd Proyecto-django
```

### 3. Instalar las dependencias

Instala Django:
```shell
uv add django
```
Instala Django REST Framework:
```shell
uv add djangorestframework
```

### 4. Crear el proyecto de Django

Entra en la carpeta src:
```shell
cd src
```


Luego ejecuta:
```shell
uv run django-admin startproject nucleo .
```

Importante: no olvides el . al final del comando.
Este punto indica que el proyecto de Django debe crearse en el directorio actual.

### 5. Ejecutar el servidor

Desde la carpeta src, ejecuta:
```shell
uv run manage.py runserver
```

Si todo está correctamente configurado, Django iniciará el servidor de desarrollo.

Por defecto podrás acceder a:
```shell
http://127.0.0.1:8000/
```


# Comandos rápidos
Crear un proyecto nuevo
```shell
uv init Proyecto-django
cd Proyecto-django
uv add django
uv add djangorestframework
cd src
uv run django-admin startproject nucleo .
uv run manage.py runserver
```

Trabajar con un repositorio existente
```shell
git clone git@github.com:FacuLemo/drf-2026.git
cd drf-2026
uv sync
cd src
uv run manage.py migrate
uv run manage.py runserver
```

# Estructura básica del proyecto

Después de crear el proyecto, la estructura será similar a:
```shell
Proyecto-django/
├── .python-version
├── pyproject.toml
├── uv.lock
└── src/
    ├── manage.py
    └── nucleo/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

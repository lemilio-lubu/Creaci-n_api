# Proyecto de Gestión de Productos

Este proyecto es una API para la gestión de productos utilizando FastAPI y SQLModel. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre productos en una base de datos SQLite.

## Requisitos

- Python 3.10+
- FastAPI
- SQLModel
- Uvicorn
- pytest

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/proyecto_gestion_productos.git
    cd proyecto_gestion_productos
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    .\venv\Scripts\activate  # En Windows
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicia la aplicación:

    ```bash
    uvicorn api:app --reload
    ```

## Uso

Puedes utilizar Postman para interactuar con la API. Asegúrate de que el servidor esté en funcionamiento y utiliza las siguientes rutas para realizar operaciones CRUD:

- **Crear producto**: `POST /productos`
- **Leer productos**: `GET /productos`
- **Actualizar producto**: `PUT /productos/{id}`
- **Eliminar producto**: `DELETE /productos/{id}`

## Pruebas

Para ejecutar las pruebas, utiliza pytest:

```bash
pytest

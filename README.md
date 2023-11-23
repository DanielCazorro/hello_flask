# hello-flask

Este proyecto utiliza Flask para crear una aplicación web simple para gestionar movimientos financieros.

## Cómo lanzar el programa en desarrollo

1. Crear un entorno virtual

   ```
   # Windows
   python -m venv env

   # Mac / Linux
   python3 -m venv env
   ```

2. Activar el entorno virtual

   ```
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate
   ```

3. Instalar las dependencias

   ```
   pip install -r requirements.txt
   ```

4. Hacer una copia del archivo `.env_template` como `.env`

   ```
   # Windows
   copy .env_template .env

   # Mac / Linux
   cp .env_template .env
   ```

5. Editar el archivo `.env` y cambiar (o no) el valor de `DEBUG` (`True`/`False`)

## Estructura del proyecto

- `balance/`: Carpeta principal del proyecto.
  - `data/`: Contiene los archivos de datos (como `movimientos.csv`).
  - `static/`: Directorio para archivos estáticos (como CSS, JS, imágenes).
  - `templates/`: Plantillas HTML para las vistas de la aplicación.

- `hello.py`: Archivo principal de la aplicación Flask.

- `models.py`: Contiene las clases y la lógica para gestionar los movimientos financieros.

- `views.py`: Maneja las vistas y rutas de la aplicación Flask.

## Ejecutar la aplicación

Ejecutar `hello.py` para iniciar el servidor local.

```bash
python hello.py
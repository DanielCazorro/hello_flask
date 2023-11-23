from flask import redirect, render_template, request, url_for

from . import app
from .models import ListaMovimientos, Movimiento


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()

    return render_template("inicio.html", movs=lista.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV.
    """
    if request.method == 'GET':
        return render_template("nuevo.html")
    elif request.method == 'POST':
        return handle_post_request(request.form)

def handle_post_request(form_data):
    """
    Maneja la lógica del formulario POST para agregar un movimiento.
    """
    movimiento = Movimiento(form_data)
    if movimiento.has_errors:
        return f'Error en el nuevo movimiento. {movimiento.errores}'
    
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    lista.agregar(movimiento)
    
    return redirect(url_for('home'))

@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento.
    """
    return "Actualizar movimiento"


@app.route('/borrar')
def delete():
    """
    Elimina un movimiento existente
    """
    return "Eliminar movimiento"

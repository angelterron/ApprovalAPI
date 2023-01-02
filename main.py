from flask import Flask, request
import data

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])

def crear():
    error = None
    if request.method == 'POST':
        # Si se ha recibido un objeto se realizará la inserción
        if request.data:
            try:
                # Regresar el resultado de la función insertar
                return data.insertar(request.json)
            # retornar las excepciones provocadas por la función
            except Exception as e:
                return {
                    'error': str(e)
                }
        else:
            # devolver una respuesta de error si se ha enviado un objeto vacio
            return {
                'error': 'El objeto es necesario'
            }

    return {

    }
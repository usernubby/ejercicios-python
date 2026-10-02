from flask import Flask, render_template, request, jsonify

from tabla import TablaMultiplicar
from base_datos import BaseDatos


app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template("index.html")


@app.route("/tabla", methods=["POST"])
def tabla():

    datos = request.get_json()

    try:

        numero = int(datos["numero"])

    except (TypeError, ValueError):

        return jsonify({
            "resultado": "Ingrese un número válido."
        }), 400


    tabla_objeto = TablaMultiplicar(numero)

    resultados = tabla_objeto.generar_tabla()


    base_datos = BaseDatos()

    base_datos.guardar_tabla(numero, resultados)


    return jsonify({
        "numero": numero,
        "resultados": resultados
    })


app.run(debug=True)
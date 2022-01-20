from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def paginaInicial():
    """
    hobbies = ["Futbol", "Programar", "Peliculas"]
    return render_template("index.html", nombre="Victor", apellido="Vasquez", hobbies=hobbies )
    """
    return "Hola Mundo"

@app.route('/dojo', methods=['GET'])
def paginaDojo():
    return "Hola Dojo"

@app.route('/say/<string:name>', methods=['GET'])
def sayHello(name):
    return "Hola " + name

@app.route('/repeat/<int:num>/<string:word>', methods=['GET'])
def repeatWord(num, word):
    num=int(num)
    return render_template("index.html", numero=num, palabra=word)

@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return "Lo siento! No hay respuesta, inténtalo otra vez..."

"""
@app.route('/datos', methods=['GET'])
def paginaDatos():
    return "Aquí hay datos de la web..."
"""


if __name__ == "__main__":
    app.run(debug = True)



from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        return f'<h1>Gracias, {nombre}!</h1><p>Recibimos tu dato correctamente.</p><a href="/">Volver</a>'

    return '''
        <h1>Formulario simple</h1>
        <form method="POST">
            <label for="nombre">Escribe tu nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <button type="submit">Enviar</button>
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        mensaje = request.form.get('mensaje', '')
        return render_template('gracias.html', nombre=nombre, mensaje=mensaje)

    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    nombre_curso = 'Desarrollo Web'
    docente = 'Ing. Keller Obdulio Matta Calderón'
    return render_template('inicio.html', curso=nombre_curso, profesor=docente)


if __name__ == '__main__':
    app.run(debug=True)

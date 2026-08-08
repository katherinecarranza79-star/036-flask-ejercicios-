from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return '<p>Prueba entrando a /estudiante/&lt;tu_nombre&gt;, por ejemplo /estudiante/Maria</p>'


@app.route('/estudiante/<nombre>')
def estudiante(nombre):
    return f'<h1>Hola, {nombre}!</h1><p>Bienvenido/a al curso de Desarrollo Web.</p>'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return '<h1>Inicio</h1><p>Bienvenido a mi sitio hecho con Flask.</p>'


@app.route('/contacto')
def contacto():
    return '<h1>Contacto</h1><p>Escríbeme a: correo@ejemplo.com</p>'


@app.route('/cursos')
def cursos():
    return '<h1>Cursos</h1><ul><li>Desarrollo Web</li><li>Bases de Datos</li><li>Programación I</li></ul>'


if __name__ == '__main__':
    app.run(debug=True)

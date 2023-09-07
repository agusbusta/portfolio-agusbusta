from flask import Flask, render_template
import socketio

app = Flask(__name__, template_folder='templates')

# Ruta raíz
@app.route('/')
def index():
    return render_template('index.html')

# Otras rutas y vistas se pueden agregar aquí

if __name__ == '__main__':
    socketio.run(app, debug=True)

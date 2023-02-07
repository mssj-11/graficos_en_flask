from flask import Flask, render_template
import sqlite3
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

#   Función para convertir el gráfico en una imagen.
def plot_to_img(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

#   Ruta raíz y función que se ejecute cuando se acceda a la ruta.
@app.route('/')
def index():
    con = sqlite3.connect("empleados.db")
    cur = con.cursor()
    cur.execute("SELECT nombre, edad FROM empleados")
    empleados = cur.fetchall()

    nombres = []
    edades = []

    for empleado in empleados:
        nombres.append(empleado[0])
        edades.append(empleado[1])
    
    plt.bar(nombres, edades)
    plot = plot_to_img(plt)

    return render_template('index.html', plot=plot)

if __name__ == '__main__':
    app.run()
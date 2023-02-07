from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)

@app.route("/")
def index():
    # Crea un gráfico de barras con datos ficticios para la cantidad de empleados por departamento
    departamentos = ['Ventas', 'Desarrollo', 'Marketing', 'Recursos Humanos']
    empleados = [15, 20, 18, 17]

    fig, ax = plt.subplots()
    ax.bar(departamentos, empleados)
    ax.set_xlabel("Departamentos")
    ax.set_ylabel("Número de empleados")

    # Convierte la figura a una imagen PNG
    pngImage = io.BytesIO()
    plt.savefig(pngImage, format='png')
    pngImage.seek(0)
    encodedImage = base64.b64encode(pngImage.getvalue()).decode('utf-8')

    return render_template("index.html", encodedImage=encodedImage)


if __name__ == "__main__":
    app.run(debug=True)
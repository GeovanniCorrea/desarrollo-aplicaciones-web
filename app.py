from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/productos")
def productos():

    productos = [
        {
            "nombre": "Cemento",
            "categoria": "Materiales",
            "unidad": "Quintal",
            "stock": 150
        },
        {
            "nombre": "Acero",
            "categoria": "Estructura",
            "unidad": "Quintal",
            "stock": 80
        },
        {
            "nombre": "Arena",
            "categoria": "Materiales",
            "unidad": "m³",
            "stock": 50
        },
        {
            "nombre": "Grava",
            "categoria": "Materiales",
            "unidad": "m³",
            "stock": 0
        }
    ]

    titulo = "Inventario de materiales"

    return render_template(
        "productos.html",
        productos=productos,
        titulo=titulo
    )


@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")


@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")


if __name__ == "__main__":
    app.run(debug=True)
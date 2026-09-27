from flask import Flask, render_template

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "clave-secreta-constructpro"


# =========================
# INICIO
# =========================

@app.route("/")
def inicio():
    return render_template("index.html")


# =========================
# PRODUCTOS
# =========================

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


@app.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():

    form = ProductoForm()

    if form.validate_on_submit():

        return "Producto procesado correctamente."

    return render_template(
        "formulario_producto.html",
        form=form
    )


# =========================
# CLIENTES
# =========================

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


@app.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():

    form = ClienteForm()

    if form.validate_on_submit():

        return "Cliente procesado correctamente."

    return render_template(
        "formulario_cliente.html",
        form=form
    )


# =========================
# PROVEEDORES
# =========================

@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")


@app.route("/proveedores/nuevo", methods=["GET", "POST"])
def nuevo_proveedor():

    form = ProveedorForm()

    if form.validate_on_submit():

        return "Proveedor procesado correctamente."

    return render_template(
        "formulario_proveedor.html",
        form=form
    )


# =========================
# FACTURACIÓN
# =========================

@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")


@app.route("/facturacion/nuevo", methods=["GET", "POST"])
def nueva_factura():

    form = FacturacionForm()

    if form.validate_on_submit():

        return "Factura procesada correctamente."

    return render_template(
        "formulario_facturacion.html",
        form=form
    )


# =========================
# EJECUTAR APLICACIÓN
# =========================

if __name__ == "__main__":
    app.run(debug=True)


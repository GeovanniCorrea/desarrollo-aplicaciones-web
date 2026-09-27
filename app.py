from flask import Flask, render_template, redirect, url_for
import sqlite3
import os

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "clave-secreta-constructpro"


# =========================
# BASE DE DATOS
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

DATABASE = os.path.join(DATA_DIR, "ferreteria.db")


def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


def init_db():

    os.makedirs(DATA_DIR, exist_ok=True)

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            unidad TEXT NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    conn.commit()

    conn.close()


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

    conn = get_db_connection()

    productos = conn.execute("""
        SELECT id, nombre, categoria, unidad, stock
        FROM productos
        ORDER BY id DESC
    """).fetchall()

    conn.close()

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

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO productos
            (nombre, categoria, unidad, stock)
            VALUES (?, ?, ?, ?)
        """, (
            form.nombre.data,
            form.categoria.data,
            form.unidad.data,
            form.stock.data
        ))

        conn.commit()

        conn.close()

        return redirect(url_for("productos"))

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

    init_db()

    app.run(debug=True)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProveedorForm(FlaskForm):

    proveedor = StringField(
        "Proveedor",
        validators=[
            DataRequired(message="El proveedor es obligatorio."),
            Length(min=3, max=80, message="Debe tener entre 3 y 80 caracteres.")
        ]
    )

    producto_servicio = StringField(
        "Producto o servicio",
        validators=[
            DataRequired(message="Este campo es obligatorio."),
            Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres.")
        ]
    )

    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Length(min=7, max=15, message="Ingrese un teléfono válido.")
        ]
    )

    ciudad = StringField(
        "Ciudad",
        validators=[
            DataRequired(message="La ciudad es obligatoria."),
            Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres.")
        ]
    )

    submit = SubmitField("Guardar proveedor")
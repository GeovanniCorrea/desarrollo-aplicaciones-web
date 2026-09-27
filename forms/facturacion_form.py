from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class FacturacionForm(FlaskForm):

    numero = StringField(
        "Número de factura",
        validators=[
            DataRequired(message="El número de factura es obligatorio."),
            Length(min=5, max=20, message="Ingrese un número de factura válido.")
        ]
    )

    cliente = StringField(
        "Cliente",
        validators=[
            DataRequired(message="El cliente es obligatorio."),
            Length(min=3, max=80, message="Debe tener entre 3 y 80 caracteres.")
        ]
    )

    proyecto = StringField(
        "Proyecto",
        validators=[
            DataRequired(message="El proyecto es obligatorio."),
            Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres.")
        ]
    )

    fecha = DateField(
        "Fecha",
        validators=[
            DataRequired(message="La fecha es obligatoria.")
        ],
        format="%Y-%m-%d"
    )

    total = DecimalField(
        "Total",
        validators=[
            DataRequired(message="El total es obligatorio."),
            NumberRange(min=0, message="El total no puede ser negativo.")
        ]
    )

    submit = SubmitField("Guardar factura")
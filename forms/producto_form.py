from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductoForm(FlaskForm):

    nombre = StringField(
        "Nombre del producto",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres.")
        ]
    )

    categoria = StringField(
        "Categoría",
        validators=[
            DataRequired(message="La categoría es obligatoria."),
            Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres.")
        ]
    )

    unidad = StringField(
        "Unidad",
        validators=[
            DataRequired(message="La unidad es obligatoria.")
        ]
    )

    stock = IntegerField(
        "Stock",
        validators=[
            DataRequired(message="El stock es obligatorio."),
            NumberRange(min=0, message="El stock no puede ser negativo.")
        ]
    )

    submit = SubmitField("Guardar producto")
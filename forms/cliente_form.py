from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ClienteForm(FlaskForm):

    nombre = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres.")
        ]
    )

    empresa = StringField(
        "Empresa",
        validators=[
            DataRequired(message="La empresa es obligatoria."),
            Length(min=3, max=80, message="Debe tener entre 3 y 80 caracteres.")
        ]
    )

    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Length(min=7, max=15, message="Ingrese un teléfono válido.")
        ]
    )

    correo = StringField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo es obligatorio."),
            Email(message="Ingrese un correo electrónico válido.")
        ]
    )

    submit = SubmitField("Guardar cliente")
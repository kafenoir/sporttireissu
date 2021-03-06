from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=2,max=16, message='Virheellinen käyttäjänimi')])
    password = PasswordField("Salasana", [validators.Length(min=5,max=32, message='Virheellinen salasana')])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2,max=32, message='Nimen pituuden tulee olla 2-32 merkkiä')])
    username = StringField("Käyttäjänimi", [validators.Length(min=2,max=16, message='Käyttäjänimen pituuden tulee olla 2-16 merkkiä')])
    password = PasswordField("Salasana", [validators.Length(min=5, max=32, message='Salasanan pituuden tulee olla 5-32 merkkiä')])
    email = EmailField("Sähköpostiosoite", [validators.Email(message='Syötä sähköpostisoite (***@***.***)')])
    address = StringField("Osoite", [validators.length(min=3, max=50, message='Osoitteen pituuden tulee olla 3-50 merkkiä')])

    class Meta:
        csrf = False
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, validators

class TripForm(FlaskForm):
    name = StringField("Matkan nimi",[validators.Length(min=2, message='Matkan nimen pituuden on oltava vähintään 2 merkkiä')])
    sport = SelectField("Laji", choices=[(1, 'Juoksu'), (2, 'Pyöräily'), (3, 'Uinti')])
    destination = StringField("Kohde", [validators.Length(min=2, message='Kohteen nimen pituuden on oltava vähintään 2 merkkiä')])
    start_date = DateField("Lähtöpäivä (YYYY-KK-PP)", format='%Y-%m-%d')
    end_date = DateField("Paluupäivä (YYYY-KK-PP)", format='%Y-%m-%d')
    price = IntegerField("Hinta (€, kokonaisluku)", [validators.NumberRange(min=0, max=100001, message='Hinnan tulee olla välillä 0 - 100 000')])
    description = StringField("Kuvaus", [validators.Length(min=2, message='Kuvauksen pituuden on oltava vähintään 2 merkkiä')])
    registration_dl = DateField("Viimeinen ilmoittautumispäivä (YYYY-KK-PP)", format='%Y-%m-%d')
    max_participants = IntegerField("Max osallistujia", [validators.NumberRange(min=0, max=1001, message='Osallistujien määrän tulee olla välillä 1 - 1000')])

    class Meta:
        csrf = False
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectMultipleField, SelectField, validators, widgets
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError
from datetime import datetime
from datetime import date
from datetime import timedelta

class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TripForm(FlaskForm):
    name = StringField("Matkan nimi",[validators.Length(min=2, message='Matkan nimen pituuden on oltava vähintään 2 merkkiä')])
    destination = StringField("Kohde", [validators.Length(min=2, message='Kohteen nimen pituuden on oltava vähintään 2 merkkiä')])
    start_date = DateField('Lähtöpäivä', format='%Y-%m-%d', default=date.today() + timedelta(days=5))
    end_date = DateField("Paluupäivä", format='%Y-%m-%d', default=date.today() + timedelta(days=5))
    price = IntegerField("Hinta (€)", [validators.NumberRange(min=0, max=100001, message='Hinnan tulee olla välillä 0 - 100 000')])
    description = StringField("Kuvaus", [validators.Length(min=2, message='Kuvauksen pituuden on oltava vähintään 2 merkkiä')])
    registration_dl = DateField("Viimeinen ilmoittautumispäivä", format='%Y-%m-%d', default=date.today() + timedelta(days=3))
    max_participants = IntegerField("Max osallistujia", [validators.NumberRange(min=0, max=1001, message='Osallistujien määrän tulee olla välillä 1 - 1000')])

    sports = MultiCheckBoxField('Urheilulajit', [validators.InputRequired(message='Valitse vähintään yksi')], choices=[], coerce=int)
    levels = MultiCheckBoxField('Taitotasot', [validators.InputRequired(message='Valitse vähintään yksi')], choices=[], coerce=int)

    def validate_start_date(form, field):
        if field.data is None:
            raise ValidationError('Valitse päivämäärä')
        earliest_date = date.today() + timedelta(days=5)
        if field.data < earliest_date:
            raise ValidationError('Aikaisin lähtöpäivä on ' + earliest_date.strftime('%d-%m-%Y'))

    def validate_end_date(form, field):
        if field.data is None:
            raise ValidationError('Valitse päivämäärä')
        if field.data < form.start_date.data:
            raise ValidationError('Paluupäivä ei voi olla lähtöpäivän jälkeen.')
    
    def validate_registration_dl(form, field):
        if field.data is None:
            raise ValidationError('Valitse päivämäärä')
        if field.data > form.start_date.data - timedelta(days=2):
            raise ValidationError('Viimeisen ilmoittautumispäivän tulee olla vähintään kaksi päivää ennen lähtöä')

    class Meta:
        csrf = False

class SearchForm(FlaskForm):

    start_date = DateField('Lähtöpäivä', [validators.Optional()], format='%Y-%m-%d', default='')
    price = IntegerField("Hinta (€)", [validators.NumberRange(min=0, max=100001, message='Hinnan tulee olla välillä 0 - 100 000'), validators.Optional()])
    sports = MultiCheckBoxField('Urheilulajit', [validators.Optional()], choices=[], coerce=int)
    level = SelectField('Taitotaso', [validators.Optional()], choices=[], coerce=int)

    def validate_start_date(form, field):
        if field.data is None:
            raise ValidationError('Valitse päivämäärä')
        earliest_date = date.today() + timedelta(days=5)
        if field.data < earliest_date:
            raise ValidationError('Aikaisin lähtöpäivä on ' + earliest_date.strftime('%d-%m-%Y'))

    class Meta:
        csrf = False

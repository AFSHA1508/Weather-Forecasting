from wtforms import Form, StringField, validators

class TextForm(Form):
    city = StringField('City',[validators.Length(min=1,max=50)])
    
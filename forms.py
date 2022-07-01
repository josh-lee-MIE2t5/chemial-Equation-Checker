from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

class geteqn(FlaskForm):
    reactantsStr = StringField(label='Reactants', 
        validators=[DataRequired()])
    productsStr = StringField(label='Products', 
        validators=[DataRequired()])

    equationCheck = SubmitField(label='submit')

class backToMainPg(FlaskForm):
    backToMain = SubmitField(label = 'Check a different equation')

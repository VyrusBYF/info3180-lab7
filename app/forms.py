# pylint: disable=W0312
# pylint: disable=C0111
# pylint: disable=W0611
# pylint: disable=C0303 
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=C0301
# pylint: disable=C0326
# pylint: disable=R0903

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField, IntegerField
from wtforms.validators import InputRequired

class UploadForm():
	description = TextAreaField('Description', validators=[InputRequired()])
	photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])

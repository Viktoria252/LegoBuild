from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AddCommentForm(FlaskForm):
    body = StringField("Body", validators=[InputRequired()])
    submit = SubmitField("Post")
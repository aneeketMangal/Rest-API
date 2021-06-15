from forms.imports import *

class PostForm(FlaskForm):
    post = StringField('post', validators = [DataRequired(), Length(min = 2, max=20000)])
    submit = SubmitField('login')
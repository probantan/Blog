from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required,DataRequired
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', )
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  
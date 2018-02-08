from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Length

from isdown.utils.checker import Checker


class UrlForm(FlaskForm):
    url = StringField(
        'Enter address of the site you want to check',
        validators=[
            InputRequired(message='Enter the URL of site you want to check'),
            Length(min=5, max=255, message="URL length should be between 5 and 255 chars")
        ],
        render_kw={"placeholder": "https://google.com"}
    )
    submit = SubmitField(
        'Check'
    )

    def validate(self, *args, **kwargs):
        rv = super().validate(*args, **kwargs)
        if not rv:
            return False

        c = Checker(self.url.data)
        if not c.is_ip() and not c.is_host():
            self.url.errors.append("Provided text is not an IP address nor website address")
            return False

        return True

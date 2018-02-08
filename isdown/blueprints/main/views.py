from flask import Blueprint, render_template, redirect, url_for

from isdown.utils.checker import Checker
from .forms import UrlForm

view = Blueprint(
    'main',
    __name__
)


@view.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()

    if form.validate_on_submit():
        return redirect(url_for('.check_website', url=form.url.data))

    return render_template('main/index.jinja2', form=form)


# @view.route('/<path:url>')
@view.route('/<path:url>', methods=['GET', 'POST'])
def check_website(url):
    c = Checker(url)

    if not c.is_ip() and not c.is_host():
        return redirect(url_for('.index'))

    check = c.check()

    return render_template('main/check_website.jinja2', check=check)

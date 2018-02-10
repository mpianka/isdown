from flask import Blueprint, render_template, redirect, url_for, request, jsonify

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


@view.route('/api/', methods=['POST'])
def api_check_website():
    if 'url' not in request.json:
        return {'status': 'ERROR', 'description': "URL not provided"}

    c = Checker(request.json['url'])
    if not c.is_ip() and not c.is_host():
        return {'status': 'ERROR', 'description': "Provided URL is not valid IP nor host"}

    data = c.check()

    return jsonify({
        'status': data.code,
        'url': data.url,
        'description': data.description
    })


@view.route('/<path:url>', methods=['GET', 'POST'])
def check_website(url):
    c = Checker(url)

    if not c.is_ip() and not c.is_host():
        return redirect(url_for('.index'))

    check = c.check()

    return render_template('main/check_website.jinja2', check=check)

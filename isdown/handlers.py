from flask import current_app


@current_app.errorhandler(Exception)
def e_exception(err):
    return "Some error raised.<br/>Details:<br/>&emsp;%s" % err


@current_app.errorhandler(404)
def e_http404(err):
    return "Error 404: Not found<br/>Details:<br/>&emsp;%s" % err

class RichError(Exception):
    code = None
    message = None
    description = None
    show_user = False
    show_debug = True

    def __init__(self, code=None, message=None, description=None, show_user=False, show_debug=True):
        self.code = code
        self.message = message
        self.description = description
        self.show_user = show_user
        self.show_debug = show_debug


class TemplateNotProvidedError(RichError):
    code = 'TEMPLATE_NOT_PROVIDED'
    message = "Neither template string or path provided"
    description = "You need to specify one: template string or template path (relative to flask's config path)"

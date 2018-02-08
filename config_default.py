from datetime import timedelta


class DirectoryConfig(object):
    # Jinja2 template directory
    DIR_TEMPLATES = "_templates"

    # Static files directory
    # They're provided via flask internal server - but for prod purposes
    # i suggest to use nginx to serve them
    DIR_STATIC = "_static"


class ApplicationConfig(object):
    # handle flask's and werkzeug's exceptions in handlers.py
    # you probably wouldn't like it enabled, as it overrides debug stacktrace
    ERRORHANDLING_INTERNAL = False

    # flash mail instead of sending it in debug mode
    # caution: if you'll send 1kk mails, all will be flashed
    MAIL_FLASH_IN_DEBUG = False


class FlaskConfig(object):
    # Enable debug mode. When using the development server with flask run or app.run,
    # an interactive debugger will be shown for unhanlded exceptions,
    # and the server will be reloaded when code changes.
    DEBUG = False

    # Enable testing mode. Exceptions are propagated rather than handled by the the app’s error handlers.
    # Extensions may also change their behavior to facilitate easier testing.
    # You should enable this in your own tests.
    TESTING = False

    # Exceptions are re-raised rather than being handled by the app’s error handlers.
    # If not set, this is implicitly true if TESTING or DEBUG is enabled.
    PROPAGATE_EXCEPTIONS = None

    # Don’t pop the request context when an exception occurs.
    # If not set, this is true if DEBUG is true.
    # This allows debuggers to introspect the request data on errors,
    # and should normally not need to be set directly.
    PRESERVE_CONTEXT_ON_EXCEPTION = None

    # A secret key that will be used for securely signing the session cookie and
    # can be used for any other security related needs by extensions or your application.
    # It should be a long random string of bytes, although unicode is accepted too.
    # For example, copy the output of this to your config:
    # python -c 'import os; print(os.urandom(16))'
    # Do not reveal the secret key when posting questions or committing code.
    SECRET_KEY = None

    # If session.permanent is true, the cookie’s expiration will be set this number of seconds in the future.
    # Can either be a datetime.timedelta or an int.
    # Flask’s default cookie implementation validates that the cryptographic signature is not older than this value.
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)

    # When serving files, set the X-Sendfile header instead of serving the data with Flask.
    # Some web servers, such as Apache, recognize this and serve the data more efficiently.
    # This only makes sense when using such a server.
    USE_X_SENDFILE = False

    # Inform the application what host and port it is bound to. Required for subdomain route matching support.
    # If set, will be used for the session cookie domain if SESSION_COOKIE_DOMAIN is not set.
    # Modern web browsers will not allow setting cookies for domains without a dot.
    # To use a domain locally, add any names that should route to the app to your hosts file.
    # ```127.0.0.1 localhost.dev```
    # If set, url_for can generate external URLs with only an application context instead of a request context.
    SERVER_NAME = None

    # Inform the application what path it is mounted under by the application / web server.
    # Will be used for the session cookie path if SESSION_COOKIE_PATH is not set.
    APPLICATION_ROOT = None

    # The name of the session cookie. Can be changed in case you already have a cookie with the same name.
    SESSION_COOKIE_NAME = 'xsesscookie'

    # The domain match rule that the session cookie will be valid for. If not set,
    # the cookie will be valid for all subdomains of SERVER_NAME.
    # If False, the cookie’s domain will not be set.
    SESSION_COOKIE_DOMAIN = None

    # The path that the session cookie will be valid for.
    # If not set, the cookie will be valid underneath `APPLICATION_ROOT` or `/` if that is not set.
    SESSION_COOKIE_PATH = None

    # Browsers will not allow JavaScript access to cookies marked as “HTTP only” for security.
    SESSION_COOKIE_HTTPONLY = True

    # Browsers will only send cookies with requests over HTTPS if the cookie is marked “secure”.
    # The application must be served over HTTPS for this to make sense.
    SESSION_COOKIE_SECURE = False

    # Control whether the cookie is sent with every response when session.permanent is true.
    # Sending the cookie every time (the default) can more reliably keep the session from expiring,
    # but uses more bandwidth. Non-permanent sessions are not affected.
    SESSION_REFRESH_EACH_REQUEST = True

    # Don’t read more than this many bytes from the incoming request data.
    # If not set and the request does not specify a CONTENT_LENGTH, no data will be read for security.
    MAX_CONTENT_LENGTH = None

    # When serving files, set the cache control max age to this number of seconds.
    # Can either be a datetime.timedelta or an int.
    # Override this value on a per-file basis using get_send_file_max_age() on the application or blueprint.
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(hours=12)

    # Trying to access a key that doesn’t exist from request dicts like args and form will
    # return a 400 Bad Request error page. Enable this to treat the error as an unhandled exception
    # instead so that you get the interactive debugger. This is a more specific version of TRAP_HTTP_EXCEPTIONS.
    # If unset, it is enabled in debug mode.
    TRAP_BAD_REQUEST_ERRORS = False

    # If there is no handler for an HTTPException-type exception,
    # re-raise it to be handled by the interactive debugger instead of returning it as a simple error response.
    TRAP_HTTP_EXCEPTIONS = False

    # Log debugging information tracing how a template file was loaded.
    # This can be useful to figure out why a template was not loaded or the wrong file appears to be loaded.
    EXPLAIN_TEMPLATE_LOADING = False

    # Use this scheme for generating external URLs when not in a request context.
    PREFERRED_URL_SCHEME = 'http'

    # Serialize objects to ASCII-encoded JSON. If this is disabled, the JSON will be returned as a Unicode string,
    # or encoded as UTF-8 by jsonify. This has security implications when rendering the JSON in to JavaScript
    # in templates, and should typically remain enabled.
    JSON_AS_ASCII = True

    # Sort the keys of JSON objects alphabetically.
    # This is useful for caching because it ensures the data is serialized the same way no matter what
    # Python’s hash seed is. While not recommended, you can disable this for a possible performance
    # improvement at the cost of caching.
    JSON_SORT_KEYS = True

    # jsonify responses will be output with newlines, spaces, and indentation for easier reading by humans.
    # Always enabled in debug mode.
    JSONIFY_PRETTYPRINT_REGULAR = True

    # The mimetype of jsonify responses.
    JSONIFY_MIMETYPE = 'application/json'

    # Reload templates when they are changed. If not set, it will be enabled in debug mode.
    TEMPLATES_AUTO_RELOAD = None

    # Logger will be disabled in flask 1.0
    # LOGGER_NAME = None
    # LOGGER_HANDLER_POLICY = 'always'


class SqlAlchemyConfig(object):
    # The database URI that should be used for the connection.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # A dictionary that maps bind keys to SQLAlchemy connection URIs.
    SQLALCHEMY_BINDS = None

    # Can be used to explicitly disable native unicode support.
    # This is required for some database adapters (like PostgreSQL on some Ubuntu versions)
    # when used with improper database defaults that specify encoding-less databases.
    SQLALCHEMY_NATIVE_UNICODE = None

    # If set to True SQLAlchemy will log all the statements issued to stderr which can be useful for debugging.
    SQLALCHEMY_ECHO = False

    # Can be used to explicitly disable or enable query recording.
    # Query recording automatically happens in debug or testing mode.
    SQLALCHEMY_RECORD_QUERIES = None

    # The size of the database pool. Defaults to the engine’s default (usually 5)
    SQLALCHEMY_POOL_SIZE = None

    # Specifies the connection timeout in seconds for the pool.
    SQLALCHEMY_POOL_TIMEOUT = None

    # Number of seconds after which a connection is automatically recycled.
    # This is required for MySQL, which removes connections after 8 hours idle by default.
    # Note that Flask-SQLAlchemy automatically sets this to 2 hours if MySQL is used.
    # Some backends may use a different default timeout value.
    SQLALCHEMY_POOL_RECYCLE = None

    # Controls the number of connections that can be created after the pool reached its maximum size.
    # When those additional connections are returned to the pool, they are disconnected and discarded.
    SQLALCHEMY_MAX_OVERFLOW = None

    # In debug mode Flask will not tear down a request on an exception
    # immediately.  Instead it will keep it alive so that the interactive
    # debugger can still access it.  This behavior can be controlled
    # by the ``PRESERVE_CONTEXT_ON_EXCEPTION`` configuration variable.
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    # If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals.
    # The default is None, which enables tracking but issues a warning that
    # it will be disabled by default in the future.
    # This requires extra memory and should be disabled if not needed.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class FlaskWtfConfig(object):
    # Set to False to disable all CSRF protection.
    WTF_CSRF_ENABLED = False

    # When using the CSRF protection extension, this controls whether every view is protected by default.
    # Default is True.
    WTF_CSRF_CHECK_DEFAULT = True

    # Random data for generating secure tokens. If this is not set then SECRET_KEY is used.
    WTF_CSRF_SECRET_KEY = None

    # HTTP methods to protect from CSRF. Default is {'POST', 'PUT', 'PATCH', 'DELETE'}.
    WTF_CSRF_METHODS = {'POST', 'PUT', 'PATCH', 'DELETE'}

    # Name of the form field and session key that holds the CSRF token.
    WTF_CSRF_FIELD_NAME = "csrf_token"

    # HTTP headers to search for CSRF token when it is not provided in the form.
    # Default is ['X-CSRFToken', 'X-CSRF-Token'].
    WTF_CSRF_HEADERS = ['X-CSRFToken', 'X-CSRF-Token']

    # Max age in seconds for CSRF tokens. Default is 3600.
    # If set to None, the CSRF token is valid for the life of the session.
    WTF_CSRF_TIME_LIMIT = 3600

    # Whether to enforce the same origin policy by checking that the referrer matches the host.
    # Only applies to HTTPS requests. Default is True.
    WTF_CSRF_SSL_STRICT = True

    # Set to False to disable Flask-Babel I18N support.
    WTF_I18N_ENABLED = True

    # Enable/disable recaptcha through SSL. Default is False.
    RECAPTCHA_USE_SSL = False

    # [required] A public key.
    RECAPTCHA_PUBLIC_KEY = None

    # [required] A private key.
    # https://www.google.com/recaptcha/admin/create
    RECAPTCHA_PRIVATE_KEY = None

    # [optional] A dict of configuration options.
    RECAPTCHA_OPTIONS = {}


class FlaskMailConfig(object):
    # SMTP server address
    MAIL_SERVER = 'localhost'

    # SMTP server port
    MAIL_PORT = 25

    # SMTP account username
    MAIL_USERNAME = None

    # SMTP account password
    MAIL_PASSWORD = None

    # Does SMTP server use TLS?
    MAIL_USE_TLS = False

    # Does SMTP server use SSL?
    MAIL_USE_SSL = False

    # What address to show in sender name? Accepts string and tuple.
    # String that would contain only e-mail address
    # or tuple with ('sender display name', 'and address')
    # Default uses account provided in MAIL_USERNAME
    MAIL_DEFAULT_SENDER = None

    # Run flask-mail in debug mode
    MAIL_DEBUG = FlaskConfig.DEBUG

    # How many e-mails server can send in one connection?
    MAIL_MAX_EMAILS = None

    # When to suspress sending e-mail?
    # Mailer class also has MAIL_FLASH_IN_DEBUG which sends mail content to front instead
    MAIL_SUPPRESS_SEND = FlaskConfig.TESTING

    # Convert attachments filenames to ASCII
    MAIL_ASCII_ATTACHMENTS = False


class DefaultConfig(
    DirectoryConfig, ApplicationConfig,
    FlaskConfig, SqlAlchemyConfig, FlaskWtfConfig, FlaskMailConfig
):
    pass

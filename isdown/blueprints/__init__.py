def register_blueprints(app):
    # main blueprint
    from .main.views import view as v_main
    app.register_blueprint(v_main)

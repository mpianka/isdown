from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_all():
    db.create_all()

# basing on the default config for the app
# which may be different from default flask (and it's extensions') values
from config_default import DefaultConfig


class Base(DefaultConfig):
    """ base config for prod, dev and testing """
    DEBUG = False
    TESTING = False


class Production(Base):
    """ production config """
    SECRET_KEY = "production key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    ERRORHANDLING_INTERNAL = True


class Development(Base):
    """ development config """
    DEBUG = True
    SECRET_KEY = "development key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class Testing(Base):
    """ testing config """
    TESTING = True
    SECRET_KEY = "testing key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

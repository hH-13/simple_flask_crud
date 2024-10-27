import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_default_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT") or "a_default_salt"
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

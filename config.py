class Config(object):
    TESTING = False
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'pythonApi'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'pythonApi'

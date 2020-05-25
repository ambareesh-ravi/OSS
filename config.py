

class Config(object):
    DEBUG = True


    JWT_SECRET_KEY = "Secret Key"

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/oss'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False



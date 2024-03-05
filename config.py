from os import environ


class BaseConfig:
    DEBUG = True
    TESTING = False
    TIMEZONE = 8
    USERNAME = environ.get('USERNAME', '')
    PASSWORD = environ.get('PASSWORD', '')

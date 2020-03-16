class Config:
    ENV = 'development'
    DEBUG = False
    TESTING = False
    APPLICATION_ROOT = '/'
    SERVER_NAME = "localhost:3000"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    ENV = 'testing'
    SERVER_NAME = 'localhost:5000'
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    SERVER_NAME = 'localhost:8080'


config = dict(
    dev=DevelopmentConfig,
    stg=TestingConfig,
    prod=ProductionConfig
)

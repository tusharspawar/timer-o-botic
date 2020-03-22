class Config:
    ENV = 'development'
    DEBUG = False
    TESTING = False
    APPLICATION_ROOT = '/'
    SERVER_NAME = "127.0.0.1:3000"


class DevelopmentConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    ENV = 'testing'
    SERVER_NAME = '127.0.0.1:5000'
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    SERVER_NAME = '127.0.0.1:8080'


config = dict(
    dev=DevelopmentConfig,
    stg=StagingConfig,
    prod=ProductionConfig
)

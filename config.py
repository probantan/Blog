import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://protus:suzy2015@localhost/blog'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass
    DEBUG = True

config_options = {
'development':DevConfig,    
'production':ProdConfig,
}


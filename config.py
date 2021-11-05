from config import SECRET_KEY
import os
class Config:
    '''
    General Configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    '''
    Production Configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development Configuration child class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
import os
class Config:
    """
    General configuration parent class
    """
    pass
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=de&category={}&apiKey={}'
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/everything?country=q=apple&from=2018-o4-09&to=2018-04-09&sortBy=popularity&apiKey={}'
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    """
    Production configuraation child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    News_api_base_url = 'https://newsapi.org/v2/top-headlines/{}?api_key{}'

class DevConfig(Config):
    """
    Development configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """

    DEBUG = True

config_options = {

    'development' : DevConfig,
    'production' : ProdConfig
}


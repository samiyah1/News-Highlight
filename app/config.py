class Config:
    """
    General configuration parent class
    """
    pass

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

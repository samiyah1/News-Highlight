from app import app
import urllib.request,json
from .models import source
from newsapi import NewsApiClient

News = news.News
# Getting api key
api_key = app.config['newsapi']

# Getting movie base url
base_url = app.config["newsapi_base_url"]

def get_news(category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        source_results = None

        if get_news_response['result']:
            news_result_list = get_news_response['results']
            news_results = process_results(news_results_list)
            
 def process_results(source_list):
        """
    Function that processes the movie result and transform them to a list of Objects

    Args:
    source_list: Aliat of dictionaries that contain movie details

    Returns :
    news_results: A list of news bjects
    """
    news_results = []
    for news_item in source_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url_path')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get ('country')

    return news_results
import urllib.request,json
from .models import Articles
from .models import Source
from app import app


# Getting api key
api_key = None
# Getting the movie base url
base_url = None
source_url = None



def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_HEAD_URL']
    source_url = app.config['NEWS_API_SOURCES_URL']
    
def get_head(category):
    '''
    Function that gets the json response to our url request
    '''
    get_head_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_head_url) as url:
        get_head_data = url.read()
        get_head_response = json.loads(get_head_data)

        news_results = None

        if get_head_response['articles']:
            news_results_list = get_head_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(new_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        new_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in new_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if author:
            news_head = Articles(id,name, author, title, description, url, urlToImage, publishedAt)
            news_results.append(news_head)

    return news_results

def get_source(category):
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            news_source_list = get_source_response['sources']
            source_results = process_source(news_source_list)
    
    return source_results

def process_source(news_results):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        new_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    source_results = []
    for item in news_results:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')
        language = item.get('language')
        country = item.get('country')


        if url:
            news_object = Source(id, name, description, url, category, language, country)
            source_results.append(news_object)

    return source_results
import urllib.request,json
from .models import news


# Getting api key
api_key = None

# Getting movie base url
sources_base_url = None
articles_base_url = None

def configuration_request(app):
    """
    Function that gets the json response to our url request
    """
   global api_key,sources_base_url,articles_base_url
   if get_source_response['result']:
       news_result_list = get_news_response['results']
       news_result = process_results(news_source_results_list)

     
            

def process_sources(news_source_results):
    """
    Function that processes the sources result and transform them to a list of Objects

    Args:
    source_list: Aliat of dictionaries that contain movie details

    Returns :
    news_results: A list of news bjects
    """
    news_source_list = []
    for source_item in news_source_results:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get ('country')

        if category:
            source_object = News(id,name,description,url,category,language,country)
            news_source_list.append(source_object)

    return news_source_list
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles

# Views


@main.route('/')
def index():
    """
	View Function that returns the index page and its data
	"""
	# Getting sources according to category
    business_news_sources = get_sources('business')
    general_news_sources = get_sources('general')
    sport_news_sources = get_sources('sport')
    entertainment_news_sources = get_sources('entertainment')
    technology_news_sources = get_sources('technology')

    title = 'Welcome to the hot News Ever'

    return render_template('index.html',title = title,business=business_news_sources,general= general_news_sources,sport=  sport_news_sources,entertainment= entertainment_news_sources,technology= technology_news_sources )


@main.route('/news_source/<id>')
def source(news_id):
    """
    View news page function that returns the news_source details page and its data
    """
    # Getting articles according to source to source chosen
    articles = get_articles(id)
    source_news_id = id.upper()
    title = f'{source_news_id} - Top Articles'

    return render_template('source.html',title=title,id=source_news_id,articles=articles)
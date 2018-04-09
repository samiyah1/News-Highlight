from flask import render_template
from app import app
from .request import get_news
# Views


@app.route('/')
def index():
    
    """
    View root page function that returns the index page and its data
    """
    # Getting popular News

    top_headline_news = get_news('top-headlines')
    sources_news = get_news('sources')
    everything_news = get_news('everything')
    title = 'Welcome to the hot News Ever'
    return render_template('index.html',title = title, top_headlines = top_headline_news,sources = sources_news,everything = everything_news)


@app.route('/news/<news_id>')
def source(news_id):
    """
    View news page function that returns the news details page and its data
    """
    return render_template('news.html',id = news_id)
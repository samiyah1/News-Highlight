from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
   # Getting Top headlines
   top-headlines_news = get_news('top-headlines')
   sources_news = get_news('sources')
   everything_news = get_news('everything')
   print(headlines_news)
   title = 'Welcome to the hot new Headlines'
    return render_template('index.html',title = title,headlines = top-headline_news)

@app.route('/news/<int:news_id>')
def source(news_id):
    """
    View news page function that returns the news details page and its data
    """
    return render_template('news.html',id = news_id)
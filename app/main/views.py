
from flask import render_template
from . import main
from ..request import get_source, get_head
# Views

@main.route('/')
def index():


    general_list = get_source('general')
    business_list = get_source('business')
    technology_list = get_source('technology')
    sports_list = get_source('sports')
    health_list = get_source('health')
    science_list = get_source('science')
    entertainment_list = get_source('entertainment')
    return render_template('index.html',general=general_list,business=business_list,technology=technology_list,sports=sports_list,health=health_list,science=science_list,entertainment=entertainment_list)

@main.route('/news/<id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    articles = get_head(id)
    return render_template('news.html', articles = articles)
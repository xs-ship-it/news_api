from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_article


#Views
@main.route('/')
def index():
    '''
    View root page function that returns data from index.html
    '''
    news = get_sources()
    title = 'Daily NEWS update'
    return render_template('index.html', title = title, news = news)

@main.route('/news/<id>')
def article(id):
    '''
    View article page that returns news data
    '''
    article = get_article(id)
    # title = f"{article.title}"

    return render_template('article.html', article = article,)

import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]

def process_sources(sources_list):
    '''
    Function that processes the news sources and transforms them to a list of objects
    '''
    sources_results = []
    for source in sources_list:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        language = source.get("language")

        source_object = Source(id,name,description,language)
        sources_results.append(source_object)

    return sources_results


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url + 'sources?apiKey=' + api_key
    print('****')
    print(get_sources_url)
    print('****')
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_articles(articles_list):
    article_results = []
    for article in articles_list:
        name = article.get("source")["name"]
        author =article.get("author")
        source = article.get("source")
        #name= source["name"]
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt")
        content = article.get("content")

        article_object = Article(author,title,description,url,urlToImage,publishedAt,content)

        article_results.append(article_object)
    return article_results

def get_article(id):
    '''
    Function that returns articles from a source
    '''
    get_article_url = base_url + 'everything?q=' + id + '&apikey=' + api_key

    with urllib.request.urlopen(get_article_url) as url:
        article_details_data =url.read()
        article_details_response = json.loads(article_details_data)

        article_results = None
        if article_details_response["articles"]:
            article_results_list = article_details_response["articles"]
            article_results = process_articles(article_results_list)

    return  article_results 

def get_movie(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            author = article_details_response.get('author')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage= article_details_response.get('urlToImage')
            publishedAt = article_details_response.get('publishedAt')
            content = article_details_response.get('content')

            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)

    return article_object
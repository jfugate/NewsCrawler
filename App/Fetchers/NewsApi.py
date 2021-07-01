import requests,os
def yieldTopHeadlines(config):
    json_response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey="+config['NewsApi_key']).json()
    for article in json_response['articles']:
        title = article['title']
        author = article['author']
        url = article['url']
        description = article['description']
        publish_time = article['publishedAt']
        yield {'title':title, 'author':author, 'description':description,'url':url, 'publish_time':publish_time}
        


from multiprocessing import Pool,freeze_support
from datetime import datetime
import time

import urllib3, requests, json, os
from bs4 import BeautifulSoup

def newsapi_yieldTopHeadlines():
    json_response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=48c9ec3bce3e484fa1429e179a08c54f").json()
    for i in range(0, len(json_response['articles'])):
        title = json_response['articles'][i]['title']
        author = json_response['articles'][i]['author']
        url = json_response['articles'][i]['url']
        description = json_response['articles'][i]['description']
        publish_time = json_response['articles'][i]['publishedAt']
        yield {'title':title, 'author':author, 'description':description,'url':url, 'publish_time':publish_time}
        
        
        
def newsapi_getTopHeadlines():
    return list(newsapi_yieldTopHeadlines())

data = [
    ("newsapi_getTopHeadlines",newsapi_getTopHeadlines)
]


def f(t):
    n,f= t
    return {n: f()}

def scanList(lst):
    s = datetime.now()
    p = Pool()
    results = p.map(f, data)
    obj  = {}
    for i in results:
        obj.update(i)
        
    e = datetime.now()
    print((e-s).seconds,"seconds")
    return obj

if __name__ == '__main__':
    freeze_support()
    a = scanList(data)
    print(a)






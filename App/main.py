from multiprocessing import Pool,freeze_support
from datetime import datetime
import Fetchers.NewsApi as NewsApi
from Libs.Caching import timed_lru_cache,getDiskCache
from Libs.Config import GetConfig

dc = getDiskCache()

@dc.memoize()
def newsapi_getTopHeadlines(config):
    return list(NewsApi.yieldTopHeadlines(config))

data = [
    ("newsapi_getTopHeadlines",newsapi_getTopHeadlines)
]


def f(t):
    n,f= t
    config = GetConfig()
    return {n: f(config)}


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
    dc['a'] = a
    print(a)






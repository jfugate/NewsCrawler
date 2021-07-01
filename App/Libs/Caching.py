
from functools import lru_cache, wraps
from datetime import datetime, timedelta


def timed_lru_cache(seconds: int = 10, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache



import diskcache as dc
cache = dc.Cache('Cache')
def getDiskCache():
    return cache

#cache[b'key'] = b'value'
#cache[b'key']
#@cache.memoize()
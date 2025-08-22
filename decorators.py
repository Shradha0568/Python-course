#decorators:
# write a decorator that measures the time a function takes to execute

import time
def timecalc(func ):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper
        
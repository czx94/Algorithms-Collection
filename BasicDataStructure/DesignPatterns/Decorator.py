def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@ log
def now():
    pass

if __name__ == '__main__':
    now()
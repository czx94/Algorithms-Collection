# using __new__

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        print(cls)
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print(self)
        pass

if __name__ == '__main__':
    singleton1 = Singleton()
    singleton2 = Singleton()
    singleton3 = Singleton()



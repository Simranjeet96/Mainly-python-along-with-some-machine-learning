def wraps(func2):
    def function(func1):
        func1.__name__=func2.__name__
        func1.__doc__=func2.__doc__
        func1.__module__=func2.__module__
        return func1
    return function    


def outerfunc(func):
    """I am outer func"""
    @wraps(func)
    def innerfunc(*args,**kwargs):
        """I am inner func"""
        print("greetings")
        func(*args,**kwargs)
        print("bye bye")

    return innerfunc    

@outerfunc
def sayHello():
    print("Hello Simranjeet Singh!!")

sayHello()
print(sayHello.__name__)
from contextlib import contextmanager

class contextManager(object):
    """docstring for contextManager"""
    
    def __init__(self, func):
        super(contextManager, self).__init__()
        self.func = func

    def __call__(self,arg1):
        self.arg1=arg1
        # self.arg2=arg2

        return self
    def __enter__(self):
        self.gen=self.func(self.arg1)
        next(self.gen)

    def __exit__(self,*args):
        try:
            # print("in exit")
            next(self.gen)
        except Exception:
            pass    

@contextManager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("foo")
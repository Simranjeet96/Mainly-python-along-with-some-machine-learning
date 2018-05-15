'''Accessing an attribute on an object like obj.foo gets you:

The result of the __get__ method of the data descriptor of the same name attached to the class if it exists

Or the corresponding value in obj.__dict__ if it exists

Or the result of the of the __get__ method of the non-data descriptor of the same name on the class

or else it falls back to look in the type(obj).__dict__

repeating for each type in the mro until it finds a match.

And assignment always creates an entry in obj.__dict__.

Unless there was a setter property (which we now know is a descriptor) in which case you’re calling a function.'''


class MyDescriptor(object):
    """docstring for MyDescriptor"""
    def __get__(self,obj,type):
        print("called __get__")
        return obj.__dict__[self.field]    
    def __set__(self,obj,val):
        print("called __set__")
        obj.__dict__[self.field] = val    

def named_descriptors(klass):
    for name, attr in klass.__dict__.items():
        if isinstance(attr, MyDescriptor):
            attr.field = name
    return klass

@named_descriptors
class MyClass(object):
        """docstring for MyClass"""
        x=MyDescriptor()

# MyClass.x=100
# print(type(MyClass.x))
obj=MyClass()
obj.x=10
print(obj.x)
obj1=MyClass()
obj1.x=11
print(obj1.x)


 

# class LazyProperty(object):
#     def __init__(self, func):
#         self._func = func
#         self.__name__ = func.__name__

#     def __get__(self, obj, klass):
#         print ("Called the func")
#         result = self._func(obj)
#         obj.__dict__[self.__name__] = result
#         return result

# class MyClass(object):
#     @LazyProperty
#     def x(self):
#         return 42

# obj=MyClass()
# print(obj.x)
# print(obj.x)
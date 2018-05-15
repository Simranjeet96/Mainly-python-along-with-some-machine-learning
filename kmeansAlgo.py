# import argparse

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--number1", help="first number")
#     parser.add_argument("--number2", help="second number")
#     parser.add_argument("--operation", help="operation", \
#                         choices=["add","subtract","multiply"])

#     args = parser.parse_args([])
#     print()

# import collections

# Person = collections.namedtuple('Person', 'name age gender')

# print ('Type of Person:', type(Person))

# bob = Person(name='Bob', age=30, gender='male')
# print ('\nRepresentation:', bob)
# a=(1,2,3)
# a=Person(*a)
# print(a)

# import os
# from contextlib import contextmanager
# @contextmanager
# def ignored(*exceptions):
#     try:
#         print(exceptions)
#         print("hhhhh")
#         yield   
#     except exceptions:
#         print('hhhh')
#         pass

# with ignored(Exception):
#     print("kkkk")
#     os.remove('lllhelloworld.py')

# from contextlib import ContextDecorator

# class makeparagraph(ContextDecorator):
#     def __enter__(self):
#         print('<p>')
#         return self

#     def __exit__(self, *exc):
#         print('</p>')
        

# @makeparagraph()
# def emit_html():
#     print('Here is some non-HTML')

# emit_html()

class Foo(object):
     def __init__(self):
       self.obj = None
       print ('created')

     def __del__(self):
         print ('destroyed')

     def show(self):
         print('showing: ',end='')
         print (self.obj)

     def store(self, obj):     print('storing ',obj)     self.obj = obj


# import weakref
# a=[1,2,3]
# b=weakref.proxy(a)


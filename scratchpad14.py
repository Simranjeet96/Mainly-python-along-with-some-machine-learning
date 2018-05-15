# def append_to(element, to=[]):
#     print(id(to))
#     to=[]
#     print(id(to))
#     to.append(element)
#     return to
# my_list = append_to(12)
# print (my_list)


# my_other_list = append_to(42)
# print (my_other_list)
# def log(original_function, logfilename="log.txt"):
#     def new_function(*args, **kwargs):
#         with open(logfilename, "w") as logfile:
#             logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))
#         return original_function(*args, **kwargs)
#     return new_function
# @log
# def my_function(message):
#     print(message)
# my_function('jkl')        



# import datetime,numpy
# print(datetime.date.today().year)
# print(type(datetime.date))






# class A: pass 
# a = A()
# type(a)
# <class '__main__.A'>
# a.__class__
# <class '__main__.A'>
# type([])
# <class 'list'>
# [].__class__
# <class 'list'>
# type(list)
# <class 'type'>
# list.__class__
# <class 'type'>
# type(A)
# <class 'type'>
# A.__class__
# <class 'type'>
# class B(object): pass
# 
# type(B)
# <class 'type'>
# b = B()
# >>> type(b)
# <class '__main__.B'>


a=lambda x : 5+x 
print(a(4))
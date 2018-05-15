	
'''nothing'''
# class A:
#     def __init__(self):
#         self.listFoo = [1, 2]
#         self.listBar = [3, 4]

#     def get_list(self, which):
#         if which == "Foo":
#             return self.listFoo
#         return self.listBar

# a = A()
# other_list = [5, 6]

#a.get_list("Foo").extend(other_list)
# b=a.get_list('Foo')+[9]
# print(b)
# knowledge = {"Frank": ["Perl"], "Monica":["C","C++"]}
# knowledge2 = {"Guido":["Python"], "Frank":["Perl", "Python"]}
# knowledge.update(knowledge2)
# print(knowledge)
# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA"]
# country_specialities_zip = zip(dishes,countries)
# print(dict(list(country_specialities_zip)))
# country_specialities_list = list(country_specialities_zip)
# country_specialities_dict = dict(country_specialities_list)
# print(country_specialities_dict)

# x = "Hallo"
# data=x.encode('utf-32')
# print(data)
# data1=data.decode('utf-32')
# print(data1)
# data=data.decode('utf-8',"replace")
# print(data)
# a='hello'
# print(dir())
# print(globals())
# a_var = 'global value'

# def outer():
#     a_var = 'enclosed value'
    
#     def inner():
#         a_var = 'local value'
#         print(a_var)
    
#     inner()

# outer()

# '''nothing'''

# import math
# import sys
# a=10
# def foo():
# 	pass
# print('dir():',dir(),'\n\n')
# #print("dir('main'):",dir(str),'\n\n')
# print("globals():",globals(),'\n\n',"locals():",locals())
# import os 
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(os.getcwd())

# print(sys.version)
# a = 'global'

# def outer():
    
#     def len(in_var):
#         print('called my len() function: ', end="")
#         l = 0
#         for i in in_var:
#             l += 1
#         return l
    
#     a = 'local'
    
#     def inner():
#         global k
#         nonlocal a
#         a += ' variable'
#     inner()
#     print('a is', a)
#     print(len(a))


# outer()

# print(len(a))
# print('a is', a)
# print('Example 1.1:', chr(int('1100111',2)))


# def square(x):
#         return (x**2)
# def cube(x):
#         return (x**3)

# funcs = [square, cube]
# for r in range(5):
#     value = list(map(lambda x: x(r), funcs))
#     print (value)

# print(dir())
# def func2(list):
#     print(list)
#     list +=[47,11]# try this list=list+[47,11] 
#     print(list)
# a=[1,2,3]
# func2(a)
# print(a)


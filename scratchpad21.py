# # import my_module.say_goodbye as gb
# from my_module.says_hello import func 
# # parser=argparse.ArgumentParser(prog="trying argparse module",usage="parsing command line")
# # parser.add_argument("input1",nargs=2)
# # # parser.add_argument("input2",nargs=3)
# # # parser.add_argument("-i","--input",type=int)
# import math
# import sys
# # args=parser.parse_args()
# # if(__name__=="__main__" ):
# # print(my_module.says_hello.func())
# print(dir(sys))
# #    print(sys.path)
# sys.path.append("C:\\Users\\simra\\Anaconda3\\pkgs")
# print(sys.path)


# numbers = [1, 2, 2, 3, 4, 4, 5]
 
# for i in reversed(numb):
#     if not numbers[i] % 2:
#         del numbers[i]

# print(numbers)        

# class zrange:
#     def __init__(self, n):
#         self.n = n

#     def __iter__(self):
#         print("in zrange")
#         return zrange_iter(self.n)

# class zrange_iter:
#     def __init__(self, n):
#         self.i = 0
#         self.n = n

#     def __iter__(self):
#         # Iterators are iterables too.
#         # Adding this functions to make them so.
#         print("in zrange_iter")
#         return self

#     def __next__(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += 1
#             return i
#         else:
#             raise StopIteration()
# z=zrange(10)
# print(list(z))
# import time 
# start=time.time()
# class reverse_iter:
#     def __init__(self,a):
#         self.a=[x for x in reversed(a)]
#     def __iter__(self):
#         return self    
#     def __next__(self):
#         for ele in self.a:
#             yield ele
#         else:
#             raise StopIteration()         


# it = reverse_iter([1, 2, 3, 4])
# print(list((x for x in range(10))))

# def integers():
#     """Infinite sequence of integers."""
#     i = 1
#     while True:
#         yield i
#         i = i + 1

# a=integers()
# b=integers()
# print(a,b,a==b)
# print(a.__next__())

# print(a.__next__())

# class test:
#     def __init__(self,list):
#         self.obj = list
#     def mult(self, x, n):
#         x*= n
#     def numtimes(self, n):
#         self.mult(self.obj, n)
# m = test([1,2,3,4])
# m.numtimes(3)
# print(m.obj)

# import types

# class Rectangle(object):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

# class Circle(object):
#     def __init__(self, radius):
#         self.radius = radius

# c = Circle(2)
# r = Rectangle(3, 4)

# # bad
# if type(r) is not type(c):
#     print("object types do not match")

# import functools

# def typeCheck(*args,**kwargs):
#     def inner1(fn):
#         def inner2(*Args,**Kwargs):

#             for t1,t2 in zip(args,Args):
#                 assert isinstance(t2,t1)
#             for key,value in kwargs.items():
#                 assert isinstance(Kwargs[key],kwargs[key])
#             fn(*Args,**Kwargs)
#         return inner2
#     return inner1

# @typeCheck(int,int,int,l=int,m=int)
# def func(*args,**kwargs):
#     print(args,kwargs)    

# func(1,2,3,l=1,m=2,n=5)        
# # print(isinstance(1,int))

# kwargs = {"arg3": 3, "arg2": "two","arg1":5}

# def func():
#     a=[1,2,3,4,5,6,7,8,9,10]
#     k=iter(a)
#     for x in k:
#         yield x
#         if x==4:
#             break
#     for x in k:
#         yield x    
# print(type(func()))

# def Func(iterable):
#     iterable = iter(iterable)
#     for x in iterable:
#         if x==4:
#             yield x
#             break
#     for x in iterable:
#         yield x
# u=[u for u in func()]
# print(u)        

# import os
# import fnmatch
# import sys
# def gen_find(filepat,top):
#     for path, dirlist, filelist in os.walk(top):
#         for name in fnmatch.filter(filelist,filepat):
#             yield os.path.join(path,name) 

# def Gen_find(filepat,top):
#     for path, dirlist, filelist in os.walk(top):
#         for filename in filelist:
#             if filepat == filename:
#                 yield os.path.join(path,filename) 

# for file in os.walk("D:\\DOCUMENTS\\codes(ml)"):
#     print(file)
# print(sys.version)



import re
a=["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
pattern = re.compile(r"(\w+)\s?(\(.com\))?")
# # pattern = re.compile(r"le")
# matches=pattern.finditer(a[0])

# for Match in matches:
#     print(Match.group(1))
for string in a:
    matches=pattern.finditer(string)
    for match in matches:
        print(match.group(1))

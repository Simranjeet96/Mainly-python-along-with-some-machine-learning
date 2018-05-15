# class Test:
#     def __init__(self):
#         self.foo=1
#         # self.__bar=2
#     def foo(self):
#         """hello there                   
#     jc"""
#         print(callable("hello"))
#     def kooo(self):
#         print("koooo"+self)    

# class Dupli(object):
#     """docstring for Dupli"""
#     def __init__(self, arg):
#         self.foo = arg
        

# print(Test.foo(1))
# # # t=Test()
# # # #t.__bar=10

# # # print(str.__len__("simran"))
# # # print(str.lower("sasAASA"))
# # # print(dir(__builtins__))
# # #print(""" hellothrwee""")

# # def my_function(a):
# #     b = a - 2
# #     return b

# # c = 3

# # if c > 2:
# #     d = my_function(5)
# #     print(d)
# # print("%d%%"%(12))
# # import math
# # print(math.pi)
# # print(round(5.81))
# # print(dir(__builtins__))

# # import socket; socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("localhost", 56318))

# # class Person:

# #     def __init__(self, first, last):
# #         self.firstname = first
# #         self.lastname = last

# #     def Name(self):
# #         return self.firstname + " " + self.lastname

# # class Employee(Person):

# #     def __init__(self, first, last, staffnum):
# #     Person(first, last)
# #        print(obj.firstname)
# #        self.staffnumber = staffnum

# #     def GetEmployee(self):
# #         return self.Name() + ", " +  self.staffnumber

# # x = Person("Marge", "Simpson")
# # y = Employee("Homer", "Simpson", "1007")

# # print(x.Name())
# # print(y.GetEmployee())

# print("hjk" and "first" and "seconf")
# fibonacci = (lambda x, x_1=1, x_2=0:x_2 if x == 0 else fibonacci(x - 1, x_1 + x_2, x_1))
# print(fibonacci)

# class MyClass:
#     def __init__(self, d):
#         self.data = d
#     def __str__(self):
#         return '[str- data: %s]' %self.data
#     def __repr__(self):
#         return '[repr- data: %s]' %self.data 

# myObjects = [MyClass('A'), MyClass('B')]
# print(MyClass('A'))        

# import argparse

# import math

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--number1", help="first number")
#     parser.add_argument("--number2", help="second number")
#     parser.add_argument("--operation", help="operation", \
#                         choices=["add","subtract","multiply"])

#     args = parser.parse_args()

#     print(args.number1)
#     print(args.number2)
#     print(args.operation)

#     n1=int(args.number1)
#     n2=int(args.number2)
#     result = None
#     if args.operation == "add":
#         result=n1+n2
#     elif args.operation == "subtract":
#         result=n1-n2
#     elif args.operation == "multiply":
#         result=n1*n2


#     print("Result:",result) 
    


def f():
    try:
        print( "a")
        return
    except:
        print( "b")
    else:
        print( "c")
    finally:
        print( "d")
        
f()        
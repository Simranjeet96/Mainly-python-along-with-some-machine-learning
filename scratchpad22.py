
# class MyDescriptor(object):
#     def __init__(self, field=""):
#         self.field = field
#     def __get__(self, obj, type):
#         print( "Called __get__")
#         if obj is None:
#             return self
#         return obj.__dict__.get(self.field)
#     def __set__(self, obj, val):
#         print( "Called __set__")
#         obj.__dict__[self.field] = val

# class MyClass(object):
#     val = MyDescriptor("val") # must put in field name manually
# def func():
#     pass
# obj1=MyClass()
# obj2=MyClass()
# obj1.val=10
# obj2.val=12
# print(obj1.val,obj2.val,obj1.__dict__,MyClass.val)
# print()
# print()
# print(type(func))

# class A(object):
    
#     def __init__(self):
#         print("hello",self)
   
#     def function(self):
#         """docstring for function in A"""
#         pass    

# def func(kk):
#     print("hello")
# class B(A):
#     def __init__(self):
#         print("there",self)
#         super().__init__()

# obj1=A()           
# obj2=A()

# print(obj1.function())
# A.function=func
# print(obj1.function)
s1 = 'public'
s2 = 'public'
print(s2 is s1)
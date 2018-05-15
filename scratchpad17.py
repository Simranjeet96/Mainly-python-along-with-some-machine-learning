# class a(object):
#     data={'a':'aaa','b':'bbb','c':'ccc'}
#     def pop(self, key, *args):
#             return self.data.pop(key, *args)#what is this mean.

# b=a()
# print(b.pop('a',{'b':'bbb'}))
# print(b.data)
# print(b.pop('a',{'b':'bbbvv'}))
# print(b.data)


# def f():
#     x = 42
#     def g():
#         global x
#         x = 43
#     print("Before calling g: " + str(x))
#     print("Calling g now:")
#     g()
#     print("After calling g: " + str(x))
    
# f()
# print("x in main: " + str(x))
# print(globals())

a=[lambda t: t for t in [1]]
b=[t for t in [0, 1, 5, 10]]
print(a)

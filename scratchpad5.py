def func():
	a=10
	print("hello")
x=input()
y=input()
print(dir(type))
'''
help(type)
print(dir(type))
print(func)'''
try:
	a=x/int(y)
except Exception as e:
	print(type(e),e)
	raise ValueError
	print(e)
finally:
	print("hello")

print(123)
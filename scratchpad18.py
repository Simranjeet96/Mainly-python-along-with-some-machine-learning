# file=open('hello.txt',mode='w')
# a=input()
# while(len(a)!=0):
# 	file.write(a)
# 	file.write('\n')
# 	a=input()
# file.close
# file=open('hello.txt',mode='r')
# print(file.readlines())

# person = {}

# properties = [
#     ("name", str),
#     ("surname", str),
#     ("age", int),
#     ("height", float),
#     ("weight", float),
# ]

# for property, p_type in properties:
#     valid_value = None

#     while valid_value is None:
#         try:
#             value = input("Please enter your %s: " % property)
#             valid_value = p_type(value)
#         except ValueError as ve:
#             print(ve)

#     person[property] = valid_value
# def make_greeting(title, name, surname, formal=True, time=None):
#     if formal:
#         fullname =  "%s %s" % (title, surname)
#     else:
#         fullname = name

#     if time is None:
#         greeting = "Hello"
#     else:
#         greeting = "Good %s" % time

#     return "%s, %s!" % (greeting, fullname)


# def foo():
# 	i=1
# 	while(True):
# 		print ("before yield", i)
# 		yield i
# 		i=i+1
# 		print ("after yield", i)
# 		print ("end")
# 		if(i>10):
# 			raise StopIteration	

# for j in foo():
# 	print(j)

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2 * np.pi, 100)	
y = 2 * np.sin(x)

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)

ax0.step(x, y)
ax0.set_title('normal spines')

ax1.plot(x, y)
ax1.set_title('bottom-left spines')

# Hide the right and top spines
ax1.spines['right'].set_visible(False)
ax1.spines	['top'].set_visible(False)
# Only show ticks on the left and bottom spines
# ax1.yaxis.set_ticks_position('left')
# ax1.xaxis.set_ticks_position('bottom')

ax2.plot(x, y)

# Only draw spine between the y-ticks
ax2.spines['left'].set_bounds(-1, 1)
# Hide the right and top spines
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax2.yaxis.set_ticks_position('right')
ax2.xaxis.set_ticks_position('top')

# Tweak spacing between subplots to prevent labels from overlapping
plt.subplots_adjust(hspace=0.5)
plt.show()


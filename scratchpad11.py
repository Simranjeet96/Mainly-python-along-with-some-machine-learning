def outerfunc(func):
	def innerfunc(*args):
		return func(*args)
	return innerfunc
i=0
@outerfunc
def display(*msg):
	global i
	if(i%2==0):
		print(*msg)
	else:
		print("hello"+str(msg)+str(msg))
	i=i+1
	

display("simran")
display("simran")
a=(1,2)

print(*a)



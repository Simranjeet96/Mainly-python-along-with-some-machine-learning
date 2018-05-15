i=0
def addOne(myFunc):
	def addOneInside():
		global i
		i=i+1
		print(id(myFunc))
		return myFunc()+1
	return addOneInside
def oldFunc():
	return 3

oldFunc=addOne(oldFunc)	 	
print(oldFunc(),i,id(oldFunc))
print(oldFunc(),i)
print(oldFunc(),i)

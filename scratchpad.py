
'''a=[2,3,4,5,6]
print(a)
a=np.array(range(10))
a=a.reshape(2,5)
print(a)
b,c=a.shape

for i in range(b) :
	sum=0
	for j in range(c) :
		sum=sum+a[i][j]
	print(sum,"of",i+1,"row")
print(np.sum(a,axis=1))	
print("another one below")
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y=[]
for i in range(len(x)) :
	y.append("[]")
	y[i]=x[i]+v
for i in range(len(x)) :
	print(y[i])
	
print(x[0])
super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
try :
	print(super_villains["fiddler"])
except :
	pass
for x in super_villains :
	print(x,super_villains[x])'''

print(__name__)
from collections import namedtuple

import numpy as np
sum=[]
for  i in range(2000):
	a=np.random.uniform(low=1,high=7,size=1).astype(int)
	b=np.random.uniform(low=1,high=7,size=1).astype(int)
	sum.append(int(a+b))
sol=[]
import random
while(len(sum)!=0):
	a=sum[0]
	count=1
	if(len(sum)!=1):
		for i in range(1,len(sum)):
			if(sum[i]==a):
				count=count+1
	for i in range(count) :
		sum.remove(a)	
	sol.append((a,count))
import matplotlib.pyplot as plt
a=[i[0] for i in sol]
b=[i[1] for i in sol]

plt.bar(a,b,color='red')
plt.xticks(a)
plt.show()

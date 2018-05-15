'''import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_subplot(211)
ax.plot([1,2,3,4], [1,5,7,9], label='line 1', linewidth=5,color='green', linestyle='solid', marker='o',markerfacecolor='blue', markersize=12,fillstyle='left',alpha=0.3)
ax=fig.add_subplot(212)
ax.scatter([1,2,3,4], [1,4,9,16],color='green',marker='*',s=400,alpha=0.5)
ax.set_xticks([i for i in np.arange(0,21,2.5)])
ax.set_yticks([i for i in np.arange(0,21,2.5)])
plt.legend()
plt.show()
'''

####################################################

'''import matplotlib.pyplot as plt
fig1=plt.figure(1)            
ax1=fig1.add_subplot(221)
ax1.plot([1, 2, 3])
ax2=fig1.add_subplot(222)
ax2.plot([4, 5, 6])
fig2=plt.figure(2)         
ax=fig2.add_subplot(111)
ax.plot([4, 5, 6])         
ax3=fig1.add_subplot(212)
ax3.set_title('Easy hmm!') 
ax3.plot([9,10,11])
ax1.annotate('local max', xy=(2, 10), xytext=(3, 11),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax1.text(2, 10, "sssssssssssssssssssssss", bbox=dict(facecolor='red', alpha=0.3))
plt.show()'''

####################################################################

'''import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()'''
'''import numpy as np
import matplotlib.pyplot as plt
a=np.random.randn(10000)
bins=int((a.max()-a.min())/0.1)
plt.hist(a,bins=bins,color='green')
plt.show()'''

##########################################################

'''import matplotlib.pyplot as plt
import numpy as np 
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins=bins,rwidth=0.9,orientation='horizontal',label="with yticks and orientation",color='g',alpha=0.7)
plt.yticks(bins)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
plt.hist(population_ages, bins=bins, rwidth=0.9,label='without xticks',color='g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
plt.hist(population_ages, bins=bins, rwidth=0.9,label='with xticks and renaming of xvalues on x axis',orientation='vertical')
plt.xticks(bins,'as bs sc d e f g h i j k l m n'.split())
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()'''

###########################################################

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
x=np.random.uniform(low=0,high=10,size=10)
y=np.random.uniform(low=0,high=10,size=10)
z=np.random.uniform(low=0,high=10,size=10)
ax.plot(x,y,z,label="3D",linewidth=5)
ax.legend()
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")
ax.set_xticks([i for i in range(0,int(max(x)+1))])
ax.set_xticklabels("s i m r a n j e e t".split( ))
ax.set_yticks([i for i in range(0,int(max(y)+1))])
ax.set_zticks([i for i in range(0,int(max(z)+1))])
plt.show()



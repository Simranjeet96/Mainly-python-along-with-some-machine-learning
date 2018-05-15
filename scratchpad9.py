import numpy as np
d1 = np.random.random_integers(1, 7, 10)
d2 = np.random.uniform(low=1,high=7, size=10).astype(int)
print("d2->",d2)
print("d1->",d1)
import matplotlib.pyplot as plt
binwidth=1
fig=plt.figure(1)
ax1=fig.add_subplot(111)
ax1.hist([d2,d1],bins=np.arange(min(min(d1),min(d2)),max(max(d1),max(d2))+binwidth,binwidth),stacked=True,color=['red','blue'])
ax1.grid(True)
ax1.set_xticks([i for i in range(13)])
plt.show()
fig=plt.figure(2)
ax2=fig.add_subplot(111)
ax2.grid(True)
ax2.hist(d2,bins=[i for i in range(1,7,1)],width=1)
ax2.set_xticks([i for i in range(13)])

plt.show()


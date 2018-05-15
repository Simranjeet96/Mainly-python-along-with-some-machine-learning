import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
pt = pd.read_csv(r'C:\Users\simra\ML\data.csv')
points=np.array(pt)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for m in range(0,100,4):
	for b in range(0,100,4):
		sum=0
		for x,y in points:
			sum=sum+(y - (m*x + b))**2
		ax.scatter(m,b,sum)
plt.show()
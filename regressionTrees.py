# Decision Tree Regression

# Importing the libraries
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
data=[(x,y) for x in np.arange(0,1.0,0.001) for y in np.arange(0,1.0,0.001) if x**2+y**2==1.0 ]
dataDict={'x1':[],'x2':[]}
for i,j in data:
    dataDict['x1'].append(i)
    dataDict['x2'].append(j)
dataDict['x1'].append(1)
dataDict['x2'].append(1)
dataDict['x1'].append(0.5)
dataDict['x2'].append(0.5)
dataDict['x1'].append(0.7)
dataDict['x2'].append(0.7)
dataDict['x1'].append(np.random.random())
dataDict['x2'].append(np.random.random())
dataDict['x1'].append(np.random.random())
dataDict['x2'].append(np.random.random())
dataDict['x1'].append(np.random.random())
dataDict['x2'].append(np.random.random())
dataDict['x1'].append(np.random.random())
dataDict['x2'].append(np.random.random())
dataDict['x1'].append(np.random.random())
dataDict['x2'].append(np.random.random())
dataDict['x1'].append(np.random.random())
dataDict['x2'].append(np.random.random())
dataDict['y']=[1 for i in range(len(dataDict['x1']))]   
print(dataDict)

dataset = pd.DataFrame(dataDict)
X = dataset.iloc[:, 0:2].values
y = dataset.iloc[:, 2].values
print(X,y)
# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0,max_leaf_nodes=2)
regressor.fit(X, y)


fig = plt.figure()
ax = fig.gca(projection='3d')
theta=np.arange(-np.pi,np.pi,0.1)
ax.scatter(X[:,0],X[:,1], y,label='jkl',color='green')
X=[[i,j] for i,j in zip(np.sin(theta),np.cos(theta))]
print(X)
ax.plot(np.sin(theta),np.cos(theta), regressor.predict(X))
ax.scatter([0.9,0.3,0.7],[0.9,0.7,0.3], regressor.predict([[0.9,0.9],[0.7,0.7],[0.3,0.3]]),color='red')

ax.legend()
plt.show()

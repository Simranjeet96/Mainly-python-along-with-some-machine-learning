from sklearn.model_selection import StratifiedKFold
import numpy as np
X = np.random.uniform(low=10,high=40,size=10)
y = [0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
for i in range(5):
	skf = StratifiedKFold(n_splits=2,shuffle=True)
	for train, test in skf.split(X, y):
	    print("%s %s" % (train, test))
	print(end=' ')
	for i in train:    
	    print(y[i],end=' ')
	print(end='  ')
	for i in test:    
              print(y[i],end=' ')
	print("\n")    
print("*"*100)
print(type(skf.split(X, y)))
print("*"*100)
for i in range(5):
	skf = StratifiedKFold(n_splits=2)
	for train, test in skf.split(X, y):
	    print("%s %s" % (train, test))
	print("\n")        

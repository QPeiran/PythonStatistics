'''
import pandas as pd
print("sklearn_normalization.py")
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
# Get dataset
df = pd.read_csv("california_housing_train.csv", sep=",")
# Normalize total_bedrooms column
x_array = np.array(df['total_bedrooms'])
normalized_X = preprocessing.normalize([x_array])
print(x_array)
print(len(x_array))
print(normalized_X[0])
print(len(normalized_X[0]))

M =  len(normalized_X[0])
# Get column names first
names = df.columns
# Create the Scaler object
scaler = preprocessing.StandardScaler()
# Fit your data on the scaler object
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df, columns=names)


import matplotlib.pyplot as plt
plt.plot(normalized_X[0], 'ro')
#plt.ylabel('some numbers')
plt.show()
'''

# Example of the Anderson-Darling Normality Test
from scipy.stats import anderson
#data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data = [1,1,1,1,1, 11, 11, 11, 11, 11]
result = anderson(data)
print('stat=%.3f' % (result.statistic))
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < cv:
		print('Probably Gaussian at the %.1f%% level' % (sl))
	else:
		print('Probably not Gaussian at the %.1f%% level' % (sl))
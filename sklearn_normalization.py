
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


import pandas as pd
print("sklearn_normalization.py")


from sklearn import preprocessing
import numpy as np
# Get dataset
df = pd.read_csv("california_housing_train.csv", sep=",")
# Normalize total_bedrooms column
x_array = np.array(df['total_bedrooms'])
normalized_X = preprocessing.normalize([x_array])
print(df)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()



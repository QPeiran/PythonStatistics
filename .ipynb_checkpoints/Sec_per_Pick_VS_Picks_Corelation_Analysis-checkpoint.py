import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



np.random.seed()
x = np.random.random(100)
print(x)
y = 1.6*x + np.random.random(100)
print(y)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope: %f    intercept: %f r-value: %f " % (slope, intercept, r_value))

print("R-squared: %f p-value: %f" % (r_value**2, p_value) )

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()
"""
x = np.array([[0, 1], [0, 2]])
r = stats.linregress(x)
r.slope, r.intercept
"""
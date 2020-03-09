import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


"""
np.random.seed()
x = np.random.random((20,))
print(x)
y = 1.6*x + np.random.random(20)
print(y)
"""
dataFrame = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\secperpickVSpicks.csv')


sec_per_pick = dataFrame['Sec per Pick (pure production)']
picks = dataFrame['Picks']

slope, intercept, r_value, p_value, std_err = stats.linregress(picks, sec_per_pick)
print("slope: %f    intercept: %f r-value: %f " % (slope, intercept, r_value))

print("R-squared: %f p-value: %f" % (r_value**2, p_value) )

plt.plot(picks, sec_per_pick, 'o', label='original data')
plt.plot(picks, intercept + slope*picks, 'r', label='fitted line')
plt.legend()
plt.show()
"""
x = np.array([[0, 1], [0, 2]])
r = stats.linregress(x)
r.slope, r.intercept
"""
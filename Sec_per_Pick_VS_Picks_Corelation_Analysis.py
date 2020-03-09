import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


"""
np.random.seed()
x = np.random.random((20,)).
print(x)
y = 1.6*x + np.random.random(20)
print(y)

x = np.array([[0, 1], [0, 2]])
r = stats.linregress(x)
r.slope, r.intercept
"""
dataFrame = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\secperpickVSpicks.csv')

##################Line Regression Check
sec_per_pick = dataFrame['Sec per Pick (pure production)']
picks = dataFrame['Picks']

slope, intercept, r_value, p_value, std_err = stats.linregress(picks, sec_per_pick)
print("slope: %f    intercept: %f r-value: %f " % (slope, intercept, r_value))

print("R-squared: %f p-value: %f" % (r_value**2, p_value) )

plt.plot(picks, sec_per_pick, 'o', label='original data')
plt.plot(picks, intercept + slope*picks, 'r', label='fitted line')
plt.legend()
plt.show()


################Box plot group by picks###########

UniquePicks = dataFrame.Picks.unique()
DataFrameDict = {elem : pd.DataFrame for elem in UniquePicks}
for key in DataFrameDict.keys():
    DataFrameDict[key] = dataFrame[:][dataFrame.Picks == key]
    DataFrameDict[key] = DataFrameDict[key].drop("Week/Recipe", axis = 1)
#Slicing the origianl data frame
DF_by_picks = pd.DataFrame(data=None)
for key in DataFrameDict.keys():
    DF_by_picks =  pd.concat([DF_by_picks, DataFrameDict[key]], axis = 1, join='outer')
#print(DF_by_picks)

DF_by_picks.plot.box()
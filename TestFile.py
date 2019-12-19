import pandas as pd
import datetime as dt
#data = pd.read_excel (r'C:\Users\Peiran Quan\Desktop\W51.xlsx') 
#print(data)
"""
df = pd.DataFrame(data, columns=['Barcode', 'Timestamp','Date','Team Leader'])

## read columns
print (df[['Barcode','Timestamp']]) # for extracting more than 1 columns , double [] is required

## read headers
print(df.columns)

## read rows
print(df.iloc[0:5])

## read [row,column]
print(df.iloc[5,3])

counter = 0

for A,B in df.iterrows():
    print(A,B['Barcode'])
    counter += 1
    if counter >= 10:
        break

## filter by "Break Start"
BSFrame = df.loc[df['Barcode'] == 'Break Start']
#print(BSFrame)
## Summary
#print(BSFrame.describe())
## Sorting -- Both 'Date' & 'Timestamps" are descending
BSFrame_sorted = BSFrame.sort_values(['Date','Timestamp'], ascending = [False,False])
print(BSFrame_sorted)
"""

staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv')
#print(staged_df["Timestamp and Date"])

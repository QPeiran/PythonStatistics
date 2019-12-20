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
def categorize_event_shift(timestamp):
    weekday_index = pd.Timestamp(timestamp).weekday()
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    weekday = switcher.get(weekday_index,'')
    hour = pd.Timestamp(timestamp).hour
    if hour in range(6,13):
        shift = 'Morning Shift'
    elif hour in range(14,22):
        shift = 'Afternoon Shift'
    else:
        shift = 'Error'
    return weekday +' '+ shift



staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv')
print(staged_df["Timestamp and Date"][1])
print(staged_df["Timestamp and Date"][2])

t1 = pd.to_datetime(staged_df["Timestamp and Date"][1])
t2 = pd.to_datetime(staged_df["Timestamp and Date"][2])
weekday = pd.Timestamp(staged_df["Timestamp and Date"][1]).weekday()
hour = pd.Timestamp(staged_df["Timestamp and Date"][1]).hour
weekday_shift = categorize_event_shift(staged_df["Timestamp and Date"][2])


InMin = pd.Timedelta(t2-t1).seconds/60.0
print(weekday_shift)
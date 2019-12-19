import pandas as pd
import datetime as dt

def activity_dependency(barcode):
    switcher = {
        'Production Start': 'Factory Closed',
        'New Recipe Start': 'Preparation/Changeover',
        'Break End': 'Production',
        'Production Finish': 'TBD'
    }
    return switcher.get(barcode, 'Production')


staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv')
#print(dataFrame['Team Leader'].describe())
df = pd.DataFrame(columns=('Event_id', 'Start Time', 'Finish Time', 'Activity', 'Recipe Name', 'Break Reasons', 'Missing Ingredients', 'Kitting Line', 'Assembly Batch', 'Event Shift', 'Team Leader', 'Pickers Count', 'Time Consumption')) #df is the event data frame

df_temp_raw = staged_df.loc[staged_df['Kitting Line'] == 'KL1']
df_temp_event = pd.DataFrame(columns=('Event_id', 'Start Time', 'Finish Time', 'Activity', 'Recipe Name', 'Break Reasons', 'Missing Ingredients', 'Kitting Line', 'Assembly Batch', 'Event Shift', 'Team Leader', 'Pickers Count', 'Time Consumption'))
#print(df_temp)
df_temp_event['Finish Time'] = df_temp_raw['Timestamp and Date']
df_temp_event['Start Time'][0] = '2019-1-1 00:00:00'
df_temp_event['Recipe Name'][0] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()]
df_temp_event['Recipe Name'][1] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()]

for i in range (len(df_temp_raw)):
    df_temp_event['Start Time'].loc[i+1] = df_temp_raw['Timestamp and Date'].loc[i]
    df_temp_event['Activity'].loc[i] = activity_dependency(df_temp_raw['Barcode'].loc[i])

for j in range (3,len(df_temp_raw)):
    reversed_index = df_temp_raw['Recipe and P'][::-1].loc[j:].first_valid_index()
    df_temp_event['Recipe Name'].loc[j] = df_temp_raw['Recipe and P'].loc[reversed_index]

print(df_temp_event)
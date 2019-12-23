import pandas as pd
import datetime as dt

def activity_dependency(barcode):
    switcher = {
        'Production Start': 'Factory Closed',
        'New Recipe Start': 'Preparation/Changeover',
        'Break End': 'Break',
        'Production Finish': 'TBD'
    }
    return switcher.get(barcode, 'Production')

def batchcode_dependency(batchcoded):
    switcher = {
        1: 'Friday Assembly',
        2: 'Saturday Assembly',
        3: 'Sunday Assembly',
        4: 'Monday Assembly',
        5: 'Tuesday Assembly',
        6: 'Wednesday Assembly',
        7: 'Thursday Assembly'
    }
    return switcher.get(batchcoded, '')

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
        shift = 'Morning'
    elif hour in range(13,22):
        shift = 'Afternoon'
    else:
        shift = 'Error'
    return weekday +' '+ shift

def time_consumption(timestamp1,timestamp2):
    t1 = pd.to_datetime(timestamp1)
    t2 = pd.to_datetime(timestamp2)
    InMin = pd.Timedelta(t2-t1).seconds/60.0
    return InMin

def count_pickers(picker):
    picker_array = picker.split(';')
    counter = 0
    for members in picker_array:
        counter = counter + 1
    return counter - 1

staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\python_data_preparation\staged.csv')  # Can change file path here
#print(dataFrame['Team Leader'].describe())
df_final = pd.DataFrame(data=None) #df is the event data frame


def main(df_temp_raw):
    df_temp_event = pd.DataFrame(columns=('Start Time', 'Finish Time', 'Activity', 'Seq Code' ,'Recipe Name', 'Break Reasons', 'Missing Ingredients', 'Kitting Line', 'Assembly Batch', 'Event Shift', 'Team Leader', 'Pickers Count', 'Time Consumption'))
    index_align = df_temp_raw.first_valid_index() # pandas is using the df_temp_raw's frame index whenever df_temp_raw is called
    df_temp_event['Finish Time'] = df_temp_raw['Timestamp and Date']
    df_temp_event['Seq Code'] = df_temp_raw['Seq Code']
    df_temp_event['Start Time'][index_align] = '2019-1-1 00:00:00'
    #df_temp_event['Recipe Name'][1] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()]
    #print(df_temp_event)
    
    for i in range (len(df_temp_raw)):
        df_temp_event['Start Time'].loc[index_align+i+1] = df_temp_raw['Timestamp and Date'].loc[index_align+i]
        df_temp_event['Activity'].loc[index_align+i] = activity_dependency(df_temp_raw['Barcode'].loc[index_align+i])
        df_temp_event['Break Reasons'].loc[index_align+i+1] = df_temp_raw['Break Reasons'].loc[index_align+i]
        df_temp_event['Missing Ingredients'].loc[index_align+i+1] = df_temp_raw['Missing Products'].loc[index_align+i]
        df_temp_event['Kitting Line'].loc[index_align+i+1] = df_temp_raw['Kitting Line'].loc[index_align+i]
        df_temp_event['Assembly Batch'].loc[index_align+i+1] = batchcode_dependency(df_temp_raw['Production Batch'].loc[index_align+i])
        df_temp_event['Time Consumption'].loc[index_align+i] = time_consumption(df_temp_event['Start Time'].loc[index_align+i], df_temp_event['Finish Time'].loc[index_align+i])
        df_temp_event['Event Shift'].loc[index_align+i] = categorize_event_shift(df_temp_event['Finish Time'].loc[index_align+i])
        df_temp_event['Team Leader'].loc[index_align+i] = df_temp_raw['Team Leader'].loc[index_align+i]
        df_temp_event['Pickers Count'].loc[index_align+i] = count_pickers(df_temp_raw['Pickers'].loc[index_align+i])
        #print(df_temp_event)
        """
        for j in range (len(df_temp_raw)):  #############################################
            print(df_temp_raw['Recipe and P'][::-1].loc[(index_align + j):])
            reversed_index = df_temp_raw['Recipe and P'][::-1].loc[(index_align + j):].first_valid_index()
        """
        df_temp_raw['Recipe and P'][index_align] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()]
        recipe_index = df_temp_raw['Recipe and P'].loc[0:index_align+i].last_valid_index()
        #print(recipe_index)
        df_temp_event['Recipe Name'].loc[index_align+i] = df_temp_raw['Recipe and P'].loc[recipe_index]
        #print(df_temp_raw['Recipe and P'].loc[recipe_index])
    #print(df_temp_event)
    return df_temp_event

for kl in range(1,9):
    df_temp_raw = staged_df.loc[staged_df['Kitting Line'] == 'KL%s'%kl]
    #print(df_temp_raw)
    seg = main(df_temp_raw)
    #print(seg)
    df_final = pd.concat([df_final, seg], sort = False)

df_final.to_csv(r'C:\Users\Peiran Quan\Desktop\python_data_preparation\prepared.csv') # Can change file path here
print("Completed!")
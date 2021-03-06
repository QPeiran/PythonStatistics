# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import datetime as dt
import re as re


# %%
#the event is depending on the barcode scanned afterwoards

def activity_dependency(barcode):
    switcher = {
        'Production Start': 'Factory Closed',
        'New Recipe Start': 'Preparation/Changeover',
        'Break End': 'Break',
        'Production Finish': 'TBD'
    }
    return switcher.get(barcode, 'Production')


# %%
# 7 days of Assembly

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


# %%
# morning shift -- 5:00 to 14:00
# afternoon shift -- 14:00 to 23:00
# Error -- Events compeleted in other time periods

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
    if hour in range(5,14):
        shift = 'Morning'
    elif hour in range(14,23):
        shift = 'Afternoon'
    else:
        shift = 'Error'
    return weekday +' '+ shift


# %%
#calculting time cost to sec

def time_consumption(timestamp1,timestamp2):
    t1 = pd.to_datetime(timestamp1)
    t2 = pd.to_datetime(timestamp2)
    InMin = pd.Timedelta(t2-t1).seconds/60.0
    return format(InMin, '.2f')


# %%
# count how many pickers for ever events (+2 to get the total amount of people on this kitting line)

def count_pickers(picker):
    pattern = re.compile(r';|_|,')  ## <- temporary solutions overhere, may change according to the labels printed
    picker_array = pattern.findall(picker)  
    return len(picker_array)
# %%
staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\python_data_preparation\staged.csv')  # Can change file path here
staged_df['Team Leader'].describe()


# %%
# copy raw df

df_final = pd.DataFrame(data=None) #df is the event data frame


# %%
def main(df_temp_raw):
    df_temp_event = pd.DataFrame(columns=('Start Time', 'Finish Time', 'Activity', 'Seq Code' ,'Recipe Name', 'Break Reasons', 'Missing Ingredients', 'Kitting Line', 'Assembly Batch', 'Event Shift', 'Team Leader', 'Pickers Count', 'Time Consumption'))
    index_align = df_temp_raw.first_valid_index() # pandas is using the df_temp_raw's frame index whenever df_temp_raw is called
    df_temp_event['Finish Time'] = df_temp_raw['Timestamp and Date']
    df_temp_event['Seq Code'] = df_temp_raw['Seq Code']
    df_temp_event['Start Time'].loc[index_align] = '2020-1-1 00:00:00'
    #df_temp_event['Recipe Name'][1] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()]
    #print(df_temp_event)
    df_temp_raw.loc[index_align, 'Recipe and P'] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()] #ignore the waring -- data type is not changing, the return is in VIEW

    for i in range (len(df_temp_raw)):
        df_temp_event['Start Time'].loc[index_align+i+1] = df_temp_raw['Timestamp and Date'].loc[index_align+i]
        df_temp_event['Activity'].loc[index_align+i] = activity_dependency(df_temp_raw['Barcode'].loc[index_align+i])
        df_temp_event['Break Reasons'].loc[index_align+i+1] = df_temp_raw['Break Reasons'].loc[index_align+i]
        df_temp_event['Missing Ingredients'].loc[index_align+i+1] = df_temp_raw['Missing Products'].loc[index_align+i]
        df_temp_event['Kitting Line'].loc[index_align+i+1] = df_temp_raw['Kitting Line'].loc[index_align+i]
        df_temp_event['Assembly Batch'].loc[index_align+i] = batchcode_dependency(df_temp_raw['Production Batch'].loc[index_align+i])
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
        #df_temp_raw['Recipe and P'][index_align] = df_temp_raw['Recipe and P'].loc[df_temp_raw['Recipe and P'].first_valid_index()]
        recipe_index = df_temp_raw['Recipe and P'].loc[0:index_align+i].last_valid_index()
        #print(recipe_index)
        df_temp_event['Recipe Name'].loc[index_align+i] = df_temp_raw['Recipe and P'].loc[recipe_index]
        #print(df_temp_raw['Recipe and P'].loc[recipe_index])
    #print(df_temp_event)
    return df_temp_event


# %%

for kl in range(1,21):
    df_temp_raw = staged_df.loc[staged_df['Kitting Line'] == 'KL%s'%kl]
    if df_temp_raw.empty:
        print("Kitting Line %r is not included!" %(kl))  # if data frame is empty
    #print(df_temp_raw)
    else:
        seg = main(df_temp_raw)
        #print(seg)
        df_final = pd.concat([df_final, seg], sort = False)
        print("Kitting Line %r Completed!" %(kl))


# %%
df_final['Week'] = '2020-40'
df_final


# %%
df_final.to_csv(r'C:\Users\Peiran Quan\Desktop\python_data_preparation\prepared.csv', index = False) # Can change file path here


# %%




# PythonStatistics

My Production Data Process Steps:

1.StagedRaw.py: Prepare the timestampe data

Step 1-1: Read raw data in Excel format, then combine 8 kitting line's data into 1 giant sheet;
(Notes: the kitting line's name is not included in raw data, it's traced by tab's name. Therefore, I add a new column with the kitting line's name)

Step 1-2: detect any missing data & remove any duplicate data;
(Notes: basically need to figure out "if all kitting line have finished all production batch")

Finally, export in CSV as "raw data staging file"



2.toDiscreteEventData.py:
Transform timestamp data to event data, the new data frame should be:
['Event_id', 'Start Time', 'Finish Time', 'Activity', 'Recipe Name', 'Break Reasons', 'Missing Ingredients', 'Kitting Line', 'Assembly Batch', 'Event Shift', 'Team Leader', 'Pickers Count', 'Time Consumption']


Step 2-1: df_event['Finish Time'] = df_staged['Timestamp and Date']
          df_event['Start Time'] = df_staged['Timestamp and Date'].(row_index + 1)

Step 2-2: df_event['Activity'] is fully depended on df_staged['Barcode']

Step 2-3: use the fisrt occured Recipe's name in the next to replace the NA
        manully fill df_staged['Recipe Name'][0&1] as the 'recipe name'; 
        reverse series/array data;
        find the first vaild cell's index;
        find the recipe name;

Step 2-3: fill in ['Break Reasons', 'Missing Ingredients', 'Kitting Line', 'Assembly Batch', 'Kitting Line', 'Assembly Batch'] with full functional dependency rules &&/|| conditional dependencies rules

Step 2-4: fill in ['Event Shift','Time Consumption'] by conditional functional dependencies rules

Step 2-5: fill in ['Team Leader', 'Pickrs Cpunt'] by CFD. However, may require nomarlize late


#pd.Timestamp("timestamp aliked data") => return a "timestamp"
#pd.Timedelta(t2-t1) => return the time difference between t1 and t2
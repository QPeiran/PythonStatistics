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
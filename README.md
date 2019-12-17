# PythonStatistics

My Production Data Process Steps:

Step 1: Read raw data in Excel format, then combine 8 kitting line's data into 1 giant sheet;
(Notes: the kitting line's name is not included in raw data, it's traced by tab's name. Therefore, I add a new column with the kitting line's name)
Step 2: detect any missing data & remove any duplicate data;
(Notes: basically need to figure out "if all kitting line have finished all production batch")




Finally, export in CSV as "raw data staging file"
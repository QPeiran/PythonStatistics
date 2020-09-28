# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import datetime as dt


# read file into data frame
data = {}
with pd.ExcelFile(r'C:\Users\Peiran Quan\Desktop\python_data_preparation\raw.xlsx') as xlsx: #Change the file path here
    data['KL1'] = pd.read_excel(xlsx,'Kit line 1',index_col = None,na_values='NA')
    data['KL2'] = pd.read_excel(xlsx,'Kit line 2',index_col = None,na_values='NA')#, skiprows=1)
    data['KL3'] = pd.read_excel(xlsx,'Kit line 3',index_col = None,na_values='NA')
    data['KL4'] = pd.read_excel(xlsx,'Kit line 4',index_col = None,na_values='NA')
    data['KL5'] = pd.read_excel(xlsx,'Kit line 5',index_col = None,na_values='NA')
    data['KL6'] = pd.read_excel(xlsx,'Kit line 6',index_col = None,na_values='NA')
    data['KL7'] = pd.read_excel(xlsx,'Kit line 7',index_col = None,na_values='NA')
    data['KL8'] = pd.read_excel(xlsx,'Kit line 8',index_col = None,na_values='NA')
    data['KL9'] = pd.read_excel(xlsx,'Kit line 9',index_col = None,na_values='NA')
    data['KL10'] = pd.read_excel(xlsx,'Kit line 10',index_col = None,na_values='NA')
    data['KL11'] = pd.read_excel(xlsx,'Kit line 11',index_col = None,na_values='NA')
    data['KL12'] = pd.read_excel(xlsx,'Kit line 12',index_col = None,na_values='NA')
    data['KL13'] = pd.read_excel(xlsx,'Kit line 13',index_col = None,na_values='NA')
    data['KL14'] = pd.read_excel(xlsx,'Kit line 14',index_col = None,na_values='NA')
    data['KL15'] = pd.read_excel(xlsx,'Kit line 15',index_col = None,na_values='NA')
    data['KL16'] = pd.read_excel(xlsx,'Kit line 16',index_col = None,na_values='NA')
    data['KL17'] = pd.read_excel(xlsx,'Kit line 17',index_col = None,na_values='NA')
    data['KL18'] = pd.read_excel(xlsx,'Kit line 18',index_col = None,na_values='NA')
    data['KL19'] = pd.read_excel(xlsx,'Kit line 19',index_col = None,na_values='NA')
    data['KL20'] = pd.read_excel(xlsx,'Kit line 20',index_col = None,na_values='NA')

# Join all kitting lines' data to one
df = pd.DataFrame(data=None)   # df is the frame containing all raw data
for KL in data:
    sLength = len(data[KL])
    KL_array = [KL for i in range(sLength)]
    data[KL]['kittingline'] = KL_array               #Meanwhile add a new column with the kitting line's name
    df = pd.concat([df,data[KL]], sort = False)
    

# %%
# rename all the column index
df.columns = ['Barcode', 'Production Batch', 'Recipe and P', 'Timestamp', 'Date', 'Seq Code', 'Week', 'Team Leader', 'Replenisher', 'Pickers', 'Break Reasons', 'Missing Products', 'Kitting Line']


# %%
df.head(10)


# %%
# type(df['Timestamp'].iloc[1]) == dt.time
type(df['Date'].iloc[0]) not in [pd._libs.tslibs.timestamps.Timestamp, 1]


# %%
# Check timestamps & date whether have the right format
def check_data_type(dataframe, col):
    for i in range(len(dataframe)):
        if type(dataframe[col].iloc[i]) not in [dt.time, pd._libs.tslibs.timestamps.Timestamp] :
            print("check the {}th data".format(i))
        else:
            pass


# %%
check_data_type(df, 'Timestamp')


# %%
check_data_type(df, 'Date')


# %%
def combine_date_time(df, datecol, timecol):
    return df.apply(lambda row: row[datecol].replace(
                                hour=row[timecol].hour,
                                minute=row[timecol].minute,
                                second=row[timecol].second),
                    axis=1)


# %%
new_c = combine_date_time(df, 'Date', 'Timestamp')
new_c


# %%
df['Timestamp and Date'] = new_c


# %%
df = df.drop_duplicates(subset = None, keep='last') # kept 'last record' for a reason


# %%
for KL in data:
    df_new = df.loc[df['Kitting Line'] == KL] # df_new is the sliced raw data of "Kitting Line(KL) Name"
    # 1.(after dropping duplicates) for every kitting line it has to contain batch code [1:5]
    i = pd.Categorical(df_new['Production Batch'])
    for j in range (1,6):
        if j not in i.categories:
            print("Warning: %r , production batch %s is not included" %(KL,j))
        else:
            print("%r production batch %s included" %(KL,j))


# %%
df.to_csv(r'C:\Users\Peiran Quan\Desktop\python_data_preparation\staged.csv',index=False)


# %%
# conda -V


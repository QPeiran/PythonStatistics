import pandas as pd

# read file into data frame
data ={}
with pd.ExcelFile(r'C:\Users\Peiran Quan\Desktop\W51.xlsx') as xlsx:
    data['KL1'] = pd.read_excel(xlsx,'Kit line 1',index_col = None,na_values='NA')
    data['KL2'] = pd.read_excel(xlsx,'Kit line 2',index_col = None,na_values='NA')#, skiprows=1)
    data['KL3'] = pd.read_excel(xlsx,'Kit line 3',index_col = None,na_values='NA')
    data['KL4'] = pd.read_excel(xlsx,'Kit line 4',index_col = None,na_values='NA')
    data['KL5'] = pd.read_excel(xlsx,'Kit line 5',index_col = None,na_values='NA')
    data['KL6'] = pd.read_excel(xlsx,'Kit line 6',index_col = None,na_values='NA')
    data['KL7'] = pd.read_excel(xlsx,'Kit line 7',index_col = None,na_values='NA')
    data['KL8'] = pd.read_excel(xlsx,'Kit line 8',index_col = None,na_values='NA')

# Join 8 kitting lines' data to one
df = pd.DataFrame(data=None)   # df is the frame containing all raw data
for KL in data:
    sLength = len(data[KL])
    KL_array = [KL for i in range(sLength)]
    data[KL]['kittingline'] = KL_array               #Meanwhile add a new column with the kitting line's name
    df = pd.concat([df,data[KL]], sort = False)
    #print(df)

# rename all the column index
df.columns = ['Barcode', 'Production Batch', 'Recipe and P', 'Timestamp', 'Date', 'Seq Code', 'Week', 'Team Leader', 'Replenisher', 'Pickers', 'Break Reasons', 'Missing Products', 'Kitting Line']

"""
# find duplicate rows
dup = df.duplicated() # return a Boolean series with "True" at the place of each duplicated rows except their first occurrence (default value of keep argument is ‘first’). Then pass this Boolean Series to [] operator of Dataframe to select the rows which are duplicate
print(dup) 

dup = df[df.duplicated()]
print(dup) # show duplicated tuples
"""
# delete duplicates
df = df.drop_duplicates(subset = None, keep='last') # kept 'last record' for a reason

# detect missing data

# df1 = df.where(df['Kitting Line'] == 'KL1') // another option
for KL in data:
    df_new = df.loc[df['Kitting Line'] == KL] # df_new is the sliced raw data of "Kitting Line(KL) Name"
    # 1.(after dropping duplicates) for every kitting line it has to contain batch code [1:4]
    i = pd.Categorical(df_new['Production Batch'])
    for j in range (1,5):
        if j not in i.categories:
            print("Warning: %r , production batch %s is not included" %(KL,j))
        else:
            print("%r production batch %s included" %(KL,j))
    # 2.Slice the raw data by Kitting Line Name, then the tuple's squence must follow the tiem sequence. Find out the errors
    #for k in range(len(df_new)):
    print(df_new.iloc[3,3].total_seconds())





#print to CSV
#df.to_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv',index=False)

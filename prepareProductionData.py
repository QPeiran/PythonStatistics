import pandas as pd

#read file into data frame
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

#Join 8 kitting lines' data to one
df = pd.DataFrame(data=None)   # df is the frame containing all raw data
for KL in data:
    sLength = len(data[KL])
    KL_array = [KL for i in range(sLength)]
    data[key]['kittingline'] = KL_array               #Meanwhile add a new column with the kitting line's name
    df = pd.concat([df,data[KL]], sort = False)
    #print(df)
    #rename all the column index


#to delete duplicates and detect missing data
df.to_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv',index=False)

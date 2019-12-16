import pandas as pd

data ={}
with pd.ExcelFile(r'C:\Users\Peiran Quan\Desktop\W51.xlsx') as xlsx:
    data['KL1'] = pd.read_excel(xlsx,'Kit line 1',index_col = None,na_values='NA')
    data['KL2'] = pd.read_excel(xlsx,'Kit line 2',index_col = None,na_values='NA')#, skiprows=1)

df = pd.DataFrame(data=None)
for key in data:
    sLength = len(data[key])
    key_array = [key for i in range(sLength)]
    data[key]['kittingline'] = key_array
    df = pd.concat([df,data[key]])
    print(df)
    #data[key].to_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv')



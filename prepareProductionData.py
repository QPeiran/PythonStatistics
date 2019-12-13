
import pandas as pd


data = pd.read_excel (r'C:\Users\Peiran Quan\Desktop\PowerBI test data.xlsx') 
df = pd.DataFrame(data, columns=['Barcode', 'Timestamp'])

print (df)

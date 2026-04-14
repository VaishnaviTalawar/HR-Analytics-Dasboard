import pandas as pd
import numpy as np

df=pd.read_csv(r'Data/Raw Data/messy_data_analytics_project.csv')
df.head(10)
print('data loaded sucessfully')
df.info()   
df.describe()
df.isnull().sum()

"Removing of duplicates"
df=df.drop_duplicates()


"Clean Text Columns"
df['Brand']=df["Brand"].str.upper().str.strip()
df['Vendor']=df["Vendor"].str.upper().str.strip()

df['Brand']=df["Brand"].str.replace('_', ' ')

'Handling Missing Values'
df['Vendor'] = df['Vendor'].fillna("Unknown")
df['Units_Sold'] = df['Units_Sold'].fillna(df['Units_Sold'].median())
df['Price_per_Unit'] = df['Price_per_Unit'].fillna(df['Price_per_Unit'].mean())

df = df.dropna(subset=['Brand'])


'Fix data types'
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

df['Units_Sold']=pd.to_numeric(df['Units_Sold'])
df['Price_per_Unit']=pd.to_numeric(df['Price_per_Unit'])
df['Cost_per_Unit']=pd.to_numeric(df['Cost_per_Unit'])


'Recalculate important coloumns'
df['Revenue']=df['Units_Sold']*df['Price_per_Unit']
df['Cost']=df['Units_Sold']*df['Cost_per_Unit']
df['Profit']=df['Revenue']*df['Cost']
df['profit_Margin']=df['Profit']/df['Revenue']


'Removing unrealstic value'
df= df[df['Units_Sold']>0]
df=df[df['Price_per_Unit']>0]
df=df[df['Units_Sold']<500]


'Featured Engineering'
df['Month']=df['Date'].dt.month
df['Year']=df['Date'].dt.year

df['Inventory Turnover Matrix']=df['Units_Sold']/df['Inventory_Level']

'Final Check'
df.isnull().sum()
df.head()

df.to_csv(r'Data/Final data/Cleaned_Data.csv', index=False)
print("Data cleaned sucessfully")
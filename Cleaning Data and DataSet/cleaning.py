import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# read csv file (-_-)
df1 = pd.read_csv('fuel_pricing.csv')
df2 = pd.read_csv('weather.csv')
df3 = pd.read_csv('data.csv')

store_temperatures = df2.groupby(['Store'])['Temperature'].mean()
print(df2.mean())
print(store_temperatures)

# ----------------------------------------------------------------------------------
# print columns and their data types
# ------------------ fuel_pricing --------------
print(50*'#')
print(df1.info())
print(50*'#')
print(df1.dtypes)
print(50*'#')

# ------------------ weather --------------
print(50*'#')
print(df2.info())
print(50*'#')
print("df2")
print(df2.dtypes)
print(50*'#')

# ------------------ data --------------
print("df3")
print(df3.info())
print(50*'#')
print(df3.dtypes)
print(50*'#')

# ------------------------------------------------------------------------------------
# print the top ten rows of each dataset

# ------------------ fuel_pricing --------------
print(50*'#')
print("top 10 rows of df1")
print(df1.head(10))

print(50*'#')

# ------------------ weather --------------
print("top 10 rows of df2")
print(df2.head(10))

print(50*'#')

# ------------------ data --------------
print("top 10 rows of df3")
print(df3.head(10))
print(50*'#')

# ------------------------------------------------------------------------------------
# print basic statistics for numeric columns
print(50*'#')

# ------------------ fuel_pricing --------------
print("statistics for df1")
print(df1.describe())

print(50*'#')

# ------------------ weather --------------
print("statistics for df2")
print(df2.describe())

print(50*'#')

# ------------------ data --------------
print("statistics for df3")
print(df3.describe())

print(50*'#')

# --------------------------------------------------------------------------------------
# Missing data

# ------------------ fuel_pricing --------------
print("missing data in d1")
print(df1.isnull().sum())

print(50*'#')

# ------------------ weather --------------
print("missing data in d2")
print(df2.isnull().sum())

print(50*'#')

# ------------------ data --------------
print("missing data in d3")
print(df3.isnull().sum())

print(50*'#')
# --------------------------------------------------------------------------------------
# Incorrect values -negative

# ------------------ fuel_pricing --------------
print('incorrect values in df1')
print(df1[df1['Store'] < 0])
print(50*'#')

print(df1[df1['Fuel_Price'] <0])

print(50*'#')

# ------------------ weather --------------
print('incorrect values in df2')
print(df2[df2['Store'] <0])
print(50*'#')

print(df2[df2['Temperature'] <0])


print(50*'#')

# ------------------ data --------------
print('incorrect values in df3')
print(df3[df3['Store'] < 0])
print(50*'#')

print(df3[df3['Category'] < 0])
print(50*'#')

print(df3[df3['Weekly_Sales'] < 0])

# --------------------------------------------------------------------------------------
# For handling missing values. i can use fillna() or dropna() methods.
# But with the ENG: Mohamed Mostafa, he told us that it is better to use fillna

# ------------------ fuel_pricing --------------
df1.fillna(df1.mean(), inplace=True)
print(df1)

print(50*'#')

# ------------------ weather --------------
df2.fillna(df2.mean(), inplace=True)
print(df2)

print(50*'#')

# ------------------ data --------------
df3.fillna(df3.mean(), inplace=True)
print(df3.head(50))

print(50*'#')

# --------------------------------------------------------------------------------------
# handling incorrect values. +positive

# ------------------ fuel_pricing --------------
# Remove rows with incorrect values in df1
df1 = df1[df1['Store'] > 0]
df1 = df1[df1['Fuel_Price'] > 0]
print(df1)

# ------------------ weather --------------
# Remove rows with incorrect values in df2
df2 = df2[df2['Store'] > 0]
df2 = df2[df2['Temperature'] > 0]
print(df2)

# ------------------ data --------------
# Remove rows with incorrect values in df3
df3 = df3[df3['Store'] > 0]
df3 = df3[df3['Category'] > 0]
df3 = df3[df3['Weekly_Sales'] > 0]
print(df3)

# --------------------------------------------------------------------------------------
# Remove duplicates
print(50*'#')

# ------------------ fuel_pricing --------------
df1.drop_duplicates(inplace=True)
print(df1)

print(50*'#')

# ------------------ weather --------------

df2.drop_duplicates(inplace=True)
print(df2)

print(50*'#')

# ------------------ data --------------

df3.drop_duplicates(inplace=True)
print(df3)

print(50*'#')

# --------------------------------------------------------------------------------------
# merge all datasets have a 'Date' and 'Store' column
merged_df1 = pd.merge(df1, df2, on=['Date', 'Store'])
merged_df2 = pd.merge(merged_df1, df3, on=['Date', 'Store'])
print(merged_df2)


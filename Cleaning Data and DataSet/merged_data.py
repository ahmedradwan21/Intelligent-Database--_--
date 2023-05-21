import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# read csv file (-_-)
df1 = pd.read_csv('fuel_pricing.csv')
df2 = pd.read_csv('weather.csv')
df3 = pd.read_csv('data.csv')

# merge all datasets have a 'Date' and 'Store' column
merged_df1 = pd.merge(df1, df2, on=['Date', 'Store'])
merged_df2 = pd.merge(merged_df1, df3, on=['Date', 'Store'])
print(merged_df2)


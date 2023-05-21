import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read csv file (-_-)
df1 = pd.read_csv('fuel_pricing.csv')
df2 = pd.read_csv('weather.csv')
df3 = pd.read_csv('data.csv')

# merge all datasets have a 'Date' and 'Store' column
merged_df1 = pd.merge(df1, df2, on=['Date', 'Store'])
merged_df2 = pd.merge(merged_df1, df3, on=['Date', 'Store'])
print(merged_df2)



#(1)Make a chart to illustrate if weekly sales are increasing or decreasing over time.
# plt.figure()
# plt.plot(merged_df['Date'], merged_df['Weekly_Sales'],color='red')
# '--bo',linewidth=1
# plt.style.use("bmh")
# Sort the merged dataframe by date
merged_df2.sort_values('Date', inplace=True)

plt.plot(merged_df2['Date'],merged_df2['Weekly_Sales'],'b--',linewidth=1)
plt.style.use("bmh")
plt.xlabel('date')
plt.ylabel('weekly sales')
plt.title('Weekly Sales Over Time (-__-)')
plt.show()

# ---------------------------------------------------------------------------------

#(2)Make a chart to show how much each brand sells.
# Groupby the data by store and sum the weekly sales
store_sales = merged_df2.groupby('Store')['Weekly_Sales'].sum()
plt.bar(store_sales.index, store_sales,color='blue',linewidth=1)
plt.style.use("bmh")
plt.xlabel('Store')
plt.ylabel('Total Sales')
plt.title('Total Sales by Store')
plt.show()

# ---------------------------------------------------------------------------------

#(3)Determine the top ten selling stores.
# Group the sales data by store and calculate the total sales for each store.
top = merged_df2.groupby('Store').sum().reset_index()
print(top)
top_store = top.sort_values('Weekly_Sales', ascending=False)[:10]
print(top_store)


# ---------------------------------------------------------------------------------

#(4)Make a histogram to show the top 10 stores sales
# Create a bar plot of weekly sales by store
plt.bar(top_store['Store'], top_store['Weekly_Sales'], linewidth=1)

# Set the chart title and axis labels
plt.title('Weekly Sales by Top 10 Stores')
plt.xlabel('Store')
plt.ylabel('Weekly Sales')
plt.show()


# ---------------------------------------------------------------------------------

#(5)Create a chart that compares average weekly sales for the top ten selling stores during holidays and non-holidays.
# Group the data by the store and holiday status, and calculate the average weekly sales
grouped = merged_df2.groupby(['Store', 'Holiday'])['Weekly_Sales'].mean().reset_index()
print(grouped)
# Select the top ten selling stores based on their average weekly sales
top_stores = merged_df2.groupby('Store')['Weekly_Sales'].mean().nlargest(10).index
print(top_stores)
# Filter the data to include only the top ten selling stores
grouped_top = grouped[grouped['Store'].isin(top_stores)]
print(grouped_top)

# Create a bar chart comparing the average weekly sales during holidays and non-holidays for the top ten selling stores

grouped_top.pivot(index='Store', columns='Holiday', values='Weekly_Sales').plot(kind='bar')
plt.title('Average Weekly Sales During Holidays and Non-Holidays for the Top Ten Selling Stores')
plt.xlabel('Store')
plt.ylabel('Average Weekly Sales')
plt.show()

# ---------------------------------------------------------------------------------

#(6) Create a chart that displays the average weekly sales for each brand department for the top 10 selling stores.
for i in top_stores:
    top_stores1 = merged_df2.loc[merged_df2['Store'] == i]
    plt.bar(top_stores1['Category'], top_stores1['Weekly_Sales'])
    plt.xlabel('brand department')
    plt.ylabel('Average Weekly Sales')
    plt.title(f"store {i}")
    plt.tight_layout(pad = 2)
    plt.show()
    
# ---------------------------------------------------------------------------------
    
#(7)Make a line chart to show the relationship between weekly sales and weather Temperature.
# Group the data by temperature and calculate the average weekly sales for each temperature
sales = merged_df2.groupby("Temperature")["Weekly_Sales"].mean()

# Plot the relationship between weekly sales and weather temperature
plt.plot(sales)
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales vs. Temperature')
plt.show()

# ---------------------------------------------------------------------------------

#(8)Make a line chart to show the relationship between the fuel_price and weekly sales.
df_fuel_sales = merged_df2[['Fuel_Price', 'Weekly_Sales']]
print(df_fuel_sales)
df_fuel_sales_mean = df_fuel_sales.groupby('Fuel_Price')['Weekly_Sales'].mean()
print(df_fuel_sales_mean)
plt.plot(df_fuel_sales_mean.index, df_fuel_sales_mean.values)
# Set the title and axis labels
plt.title('Weekly Sales vs Fuel Price')
plt.xlabel('Fuel Price')
plt.ylabel('Weekly Sales')

# Show the plot
plt.show()
# Modeling : Divides the data into training and testing categories (80 percent training data and 20 percent testing data).
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# read csv file (-_-)
df1 = pd.read_csv('fuel_pricing.csv')
df2 = pd.read_csv('weather.csv')
df3 = pd.read_csv('data.csv')

# merge all datasets have a 'Date' and 'Store' column
merged_df1 = pd.merge(df1, df2, on=['Date', 'Store'])
merged_df2 = pd.merge(merged_df1, df3, on=['Date', 'Store'])
print(merged_df2)




# Load dataset
X = merged_df2[['Temperature', 'Category', 'Store', 'Holiday']]  # Input features
y = merged_df2['Weekly_Sales']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Create two separate supervised learning models to forecast weekly sales based on specific characteristics.

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Fit the decision tree regressor on the training set
dtr = DecisionTreeRegressor()
dtr.fit(X_train, y_train)

# Use the fitted model to make predictions on the testing set
dtr_predictions = dtr.predict(X_test)

# Calculate the R-squared of the predictions
dtr_r2 = r2_score(y_test, dtr_predictions)
# Represent the R-squared as a percentage
dtr_r2_percentage = dtr_r2 * 100

# Print the R-squared as a percentage
print('Decision Tree Regression R-squared:', dtr_r2_percentage, '%')
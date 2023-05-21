import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


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


from sklearn.ensemble import GradientBoostingRegressor
# Fit the gradient boosting regression model on the training set
gbr = GradientBoostingRegressor(n_estimators=100, max_depth=4, learning_rate=0.1, random_state=42)
gbr.fit(X_train, y_train)

# Use the fitted model to make predictions on the testing set
gbr_predictions = gbr.predict(X_test)

# Calculate the R-squared of the predictions
gbr_r2 = r2_score(y_test, gbr_predictions)

# Represent the R-squared as a percentagegbr_
gbr_r2_percentage = gbr_r2 * 100

# Print the R-squared as a percentage
print('Gradient Boosting Regression R-squared:', gbr_r2_percentage, '%')



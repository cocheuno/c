import pandas as pd
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

# Read the spreadsheet
data = pd.read_excel(r'C:\Users\Owner\OneDrive\Data\Whitewater\Spring 2024\ITSCM 180\Assignments\5\air traffic.xlsx')

# Filter data for the years 2003-2022
filtered_data = data[(data['Year'] >= 2003) & (data['Year'] <= 2022)]

# Split the data into independent and dependent variables
X = filtered_data[['Year', 'Month', 'Dom_Pax', 'Dom_Flt', 'Dom_RPM', 'Dom_ASM']]
y = filtered_data['Dom_LF']

# Perform multiple regression fit
regression_model = LinearRegression()
regression_model.fit(X, y)

# Print regression statistics
X = sm.add_constant(X)  # Add constant term for intercept
new_data = data[(data['Year'] == 2023) & (data['Month'] <= 9)]
X_new = new_data[['Year', 'Month', 'Dom_Pax', 'Dom_Flt', 'Dom_RPM', 'Dom_ASM']]
X_new = sm.add_constant(X_new)  # Add constant term for intercept
y_pred = regression_model.predict(X_new)

# Calculate percentage difference between actual and predicted Dom_LF
actual_dom_lf = new_data['Dom_LF']
percentage_difference = ((y_pred - actual_dom_lf) / actual_dom_lf) * 100

# Print percentage difference for each month
for month, diff in zip(new_data['Month'], percentage_difference):
    print(f"XXXItNotUWWMonth {month}: {diff}% difference")
print(regression_model.coef_)  # Print model coefficients

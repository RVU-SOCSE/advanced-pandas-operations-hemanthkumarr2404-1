# Importing required libraries
import pandas as pd

# Creating the employee_details DataFrame
employee_details = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

# Creating the employee_salaries DataFrame
employee_salaries = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Salary': [50000, 70000, 80000, 55000, 60000]
})

# Creating the sales_region_1 DataFrame
sales_region_1 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['North', 'North', 'North', 'North', 'North'],
'Sales': [250, 300, 200, 400, 350]
})

# Creating the sales_region_2 DataFrame
# Importing required libraries
import pandas as pd

# Creating the employee_details DataFrame
employee_details = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

# Creating the employee_salaries DataFrame
employee_salaries = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Salary': [50000, 70000, 80000, 55000, 60000]
})

# Creating the sales_region_1 DataFrame
sales_region_1 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['North', 'North', 'North', 'North', 'North'],
'Sales': [250, 300, 200, 400, 350]
})

# Creating the sales_region_2 DataFrame
# Importing required libraries
import pandas as pd

# Creating the employee_details DataFrame
employee_details = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

# Creating the employee_salaries DataFrame
employee_salaries = pd.DataFrame({
'EmployeeID': [101, 102, 103, 104, 105],
'Salary': [50000, 70000, 80000, 55000, 60000]
})

# Creating the sales_region_1 DataFrame
sales_region_1 = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Region': ['North', 'North', 'North', 'North', 'North'],
'Sales': [250, 300, 200, 400, 350]
})

# Creating the sales_region_2 DataFrame
stock_prices = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Price': [150, 155, 152, 158, 160]
})
stock_prices.set_index('Date', inplace=True)

# Creating the market_volume DataFrame with 'Date' as the index
market_volume = pd.DataFrame({
'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
'Volume': [1000, 1100, 1050, 1150, 1200]
})
market_volume.set_index('Date', inplace=True)
# Display the datasets
print("Stock Prices Data:")
print(stock_prices)
print("\nMarket Volume Data:")
print(market_volume)
# Performing the join operation
# Joining market_volume to stock_prices based on their index
joined_data = stock_prices.join(market_volume, how='inner')
print("\nJoined Stock Prices and Market Volume Data:")
print(joined_data)

# Concatenating DataFrames vertically
consolidated_sales = pd.concat([sales_region_1, sales_region_2], axis=0)
print("\nConsolidated Sales Data:")
print(consolidated_sales)

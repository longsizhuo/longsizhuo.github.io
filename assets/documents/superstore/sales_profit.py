# Import pandas library as pd
import pandas as pd

# Read CSV file named 'superstore_transaction.csv' and store it in a dataframe named 'df'
df = pd.read_csv("superstore_transaction.csv")

# Remove "$" and "," from the values in the 'Profit' column and convert it to integer
df["Profit"] = df["Profit"].str.replace('$', "").str.replace(",", "").astype(int)

# Remove "$" and "," from the values in the 'Sales' column and convert it to integer
df["Sales"] = df["Sales"].str.replace('$', "").str.replace(",", "").astype(int)

# Get the index of the row with the maximum value in the 'Profit' column and store it in 'col_max_profit'
col_max_profit = df["Profit"].idxmax()
# Get the index of the row with the maximum value in the 'Sales' column and store it in 'col_max_sales'
col_max_sales = df["Sales"].idxmax()

# Store the details of the transaction with highest sales
highest_sales_info = [
    "=========================\n"
    "HIGHEST SALES TRANSACTION\n"
    "=========================\n",
    "Category: {}\n".format(df.loc[col_max_sales, "Category"]),
    "Customer Name: {}\n".format(df.loc[col_max_sales, "Customer Name"]),
    "Product Name: {}\n".format(df.loc[col_max_sales, "Product Name"]),
    "Segment: {}\n".format(df.loc[col_max_sales, "Segment"]),
    "Sub-Category: {}\n".format(df.loc[col_max_sales, "Sub-Category"]),
    "Profit: {}\n".format(df["Sales"].max()),
]

# Store the details of the transaction with the highest profit
highest_profit_info = [
    "==========================\n"
    "HIGHEST PROFIT TRANSACTION\n"
    "==========================\n",
    "Category: {}\n".format(df.loc[col_max_profit, "Category"]),
    "Customer Name: {}\n".format(df.loc[col_max_profit, "Customer Name"]),
    "Product Name: {}\n".format(df.loc[col_max_profit, "Product Name"]),
    "Segment: {}\n".format(df.loc[col_max_profit, "Segment"]),
    "Sub-Category: {}\n".format(df.loc[col_max_profit, "Sub-Category"]),
    "Profit: {}\n".format(df["Profit"].max()),
]

# Open a file named 'summary_report.txt' in 'append' mode and store it in 'file'
with open("summary_report.txt", "a") as file:
    # Write the 'highest_sales_info' details to the file
    file.write(''.join(highest_sales_info))
    file.write(''.join(highest_profit_info))

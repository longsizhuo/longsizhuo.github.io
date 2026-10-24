import pandas as pd

df = pd.read_csv("superstore_transaction.csv")
highest_sales_info = [
    "====================\n"
    "SUPERSTORE CUSTOMERS\n"
    "====================\n",
    "TOTAL: {}\n".format(df["Customer Name"].nunique(), "Category"),
]
with open("summary_report.txt", "a") as file:
    file.writelines(highest_sales_info)

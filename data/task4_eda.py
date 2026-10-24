

import pandas as pd
from pathlib import Path

# Load the CSV from the same folder as this Python file
file_path = Path(__file__).parent / "sales_data_analytics.csv"
df = pd.read_csv(file_path)

print("=" * 50)
print("TASK 4: EXPLORATORY DATA ANALYSIS")
print("=" * 50)

print("\n1. DATASET SIZE (Rows, Columns)")
print(df.shape)

print("\n2. FIRST 5 ROWS")
print(df.head().to_string(index=False))

print("\n3. MISSING VALUES IN EACH COLUMN")
print(df.isnull().sum().to_string())

print("\n4. DUPLICATE ROW COUNT")
print(df.duplicated().sum())

print("\n5. DATA TYPES")
print(df.dtypes.to_string())

print("\n6. SUMMARY STATISTICS")
print(df.describe().round(2).to_string())

print("\n7. TOTAL SALES BY PRODUCT LINE")
print(df.groupby("Product line")["Total"].sum().round(2).to_string())

print("\n8. TOTAL SALES BY BRANCH")
print(df.groupby("Branch")["Total"].sum().round(2).to_string())

print("\n9. PAYMENT METHOD COUNTS")
print(df["Payment"].value_counts().to_string())

print("\n10. AVERAGE CUSTOMER RATING")
print(round(df["Rating"].mean(), 2))

print("\nEDA COMPLETED SUCCESSFULLY")

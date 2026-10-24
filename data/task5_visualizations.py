
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
file_path = Path(__file__).parent / "sales_data_analytics.csv"
df = pd.read_csv(file_path)

# Create a folder for charts
output_folder = Path(__file__).parent / "charts"
output_folder.mkdir(exist_ok=True)

# 1. Total Sales by Product Line
sales_product = df.groupby("Product line")["Total"].sum().sort_values()
sales_product.plot(kind="barh", title="Total Sales by Product Line")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig(output_folder / "1_sales_by_product.png")
plt.show()
plt.close()

# 2. Total Sales by Branch
sales_branch = df.groupby("Branch")["Total"].sum()
sales_branch.plot(kind="bar", title="Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(output_folder / "2_sales_by_branch.png")
plt.show()
plt.close()

# 3. Payment Method Distribution
payment_counts = df["Payment"].value_counts()
payment_counts.plot(kind="pie", autopct="%1.1f%%", title="Payment Method Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(output_folder / "3_payment_distribution.png")
plt.show()
plt.close()

# 4. Quantity Sold by Product Line
quantity_product = df.groupby("Product line")["Quantity"].sum().sort_values()
quantity_product.plot(kind="barh", title="Quantity Sold by Product Line")
plt.xlabel("Total Quantity")
plt.tight_layout()
plt.savefig(output_folder / "4_quantity_by_product.png")
plt.show()
plt.close()

# 5. Average Customer Rating by Branch
rating_branch = df.groupby("Branch")["Rating"].mean()
rating_branch.plot(kind="bar", title="Average Customer Rating by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Rating")
plt.ylim(0, 10)
plt.tight_layout()
plt.savefig(output_folder / "5_rating_by_branch.png")
plt.show()
plt.close()

print("SUCCESS: All 5 charts created and saved in the charts folder.")

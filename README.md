# Sales Data Analytics Project

## 1. Project Overview
This project analyzes sales data using Python and Microsoft Power BI. It explores sales performance, product demand, branch performance, payment preferences, and customer ratings through data analysis and visualization.

## 2. Problem Statement
Raw sales data can be difficult to understand without proper analysis. This project transforms sales records into meaningful visualizations and business insights to support better decision-making.

## 3. Dataset Description
- **Records:** 1,000 rows
- **Columns:** 17
- **Format:** CSV
- **Important fields:** Date, Branch, City, Product line, Unit price, Quantity, Total, Payment, and Rating.

## 4. Tools Used
- Python
- Pandas
- Matplotlib
- Microsoft Power BI
- Git and GitHub
- Visual Studio Code

## 5. Data Cleaning Process
The dataset was loaded and inspected using Python and Pandas. The following checks were performed:
- Checked the number of rows and columns.
- Inspected column names and data types.
- Checked for missing values.
- Reviewed summary statistics and data consistency.

The missing-value check reported no missing values in the dataset.

## 6. Exploratory Data Analysis (EDA)
EDA was performed to understand the structure and characteristics of the dataset. The analysis included:
- Dataset overview and data types.
- Summary statistics.
- Sales analysis by product line.
- Sales comparison by branch.
- Quantity and customer rating analysis.

## 7. Visualizations
Five visualizations were created using Python and Matplotlib:

1. Total Sales by Product Line
2. Total Sales by Branch
3. Payment Method Distribution
4. Quantity Sold by Product Line
5. Average Customer Rating by Branch

The charts are saved in the project's `data/charts` folder.

## 8. Power BI Dashboard
An interactive dashboard was developed in Power BI with:
- Total Sales KPI card
- Total Quantity KPI card
- Average Rating KPI card
- Sales by Product Line bar chart
- Sales by Branch column chart
- City slicer for interactive filtering

The dashboard allows users to explore sales performance and compare categories and branches.

## 9. Key Insights
1. Product-line sales comparisons help identify stronger and weaker sales categories.
2. Branch-level comparisons help evaluate differences in sales performance.
3. Payment method distribution provides information about customer payment preferences.
4. Quantity sold by product line helps understand product demand.
5. The average customer rating is approximately 6.99 out of 10, highlighting the importance of monitoring customer feedback.

## 10. Business Recommendations
1. **Improve inventory planning:** Use product demand and sales trends to maintain suitable stock levels and review lower-performing categories.
2. **Improve customer experience:** Monitor ratings and feedback, address customer concerns, and provide convenient payment options.

## 11. Conclusion
This project demonstrates a basic end-to-end data analytics workflow, from dataset inspection and exploratory analysis to Python visualizations and an interactive Power BI dashboard. The analysis helps present sales information clearly and supports business decisions related to product demand, branch performance, inventory planning, and customer satisfaction.

## 12. Project Files
- `README.md` — Project documentation
- `project_plan.md` — Project plan
- `project_structure.md` — Repository structure
- `data/sales_data_analytics.csv` — Sales dataset
- `data/task4_eda.py` — EDA script
- `data/task5_visualizations.py` — Visualization script
- `data/charts/` — Generated chart images
- `Sales_Analytics_Dashboard.pbix` — Power BI dashboard file

## 13. Author
Created as a Data Analytics project for learning and practical application.


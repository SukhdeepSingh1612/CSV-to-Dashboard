# Design for Business Intelligence Dashboard - `dashboard.py`

## Module: `dashboard.py`

The `dashboard.py` module consists of a single class, `DashboardApp`, designed to generate a business intelligence dashboard using a specified dataset. The class utilizes Streamlit and Plotly for visualization, providing insights into sales data through key metrics, time-trend analysis, and other visualizations.

### Class: `DashboardApp`

The `DashboardApp` class is responsible for handling data and generating the visualizations required for the dashboard. It provides a structured approach to derive insights from data and display them effectively.

#### `__init__(self, data)`

- **Parameters:**
  - `data`: A DataFrame containing the sales data with columns such as `CustomerID`, `CustomerName`, `Region`, `Sales`, `Profit`, `Quantity`, `Discount`, and `OrderDate`.
  
- **Functionality:** 
  - Initializes the instance of the class with the provided dataset.
  - Converts `OrderDate` column to DateTime format for time-series analysis.

#### `key_metrics(self)`

- **Functionality:** 
  - Calculates key business metrics from the dataset:
    - Total Revenue: Sum of the `Sales` column.
    - Total Profit: Sum of the `Profit` column.
    - Customer Count: Unique count of `CustomerID`.
  
- **Returns:** 
  - A tuple containing Total Revenue, Total Profit, and Customer Count.

#### `sales_trend(self)`

- **Functionality:** 
  - Analyzes the monthly sales trend by resampling the data based on the `OrderDate` to aggregate sales per month.
  - Generates a time-series line chart using Plotly.

- **Returns:** 
  - A Plotly figure object representing the monthly sales trend.

#### `top_5_products_by_revenue(self)`

- **Parameters:** 
  - `n` (default=5): Number of top products to list by revenue.
  
- **Functionality:** 
  - Computes total sales per product (`CustomerName`) and selects the top `n` products based on revenue.
  - Generates a bar chart of the top products by revenue.

- **Returns:** 
  - A Plotly figure object displaying the bar chart.

#### `revenue_share_by_region(self)`

- **Functionality:** 
  - Aggregates the sales data by `Region` to calculate revenue contribution.
  - Generates a pie chart to visualize revenue share distribution across regions.

- **Returns:** 
  - A Plotly figure displaying the pie chart of revenue share by region.

#### `profit_vs_cost(self)`

- **Functionality:** 
  - Calculates the `Cost` as the difference between `Sales` and `Profit`.
  - Creates a bar chart comparing Profit and Cost for each `CustomerName`.

- **Returns:** 
  - A Plotly figure displaying the profit vs cost per product.

#### `run(self)`

- **Functionality:** 
  - Launches the Streamlit app to display the business intelligence dashboard.
  - Integrates all visualizations and metrics into a single Streamlit interface for user interaction.

### Usage Example:

```python
import pandas as pd

# Assume data is loaded from CSV or defined as a dictionary
data = {
    'CustomerID': [1001, 1002, 1003, ...],
    'CustomerName': ['Customer_1', 'Customer_2', 'Customer_3', ...],
    # Other columns...
}

df = pd.DataFrame(data)
app = DashboardApp(df)
app.run()
```

This module provides a comprehensive approach to creating a dynamic and interactive dashboard that emphasizes crucial sales insights and metrics, facilitating informed business decision-making.
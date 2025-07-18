import pandas as pd
import streamlit as st
import plotly.express as px

class DashboardApp:
    def __init__(self, data):
        self.data = data
        self.data['OrderDate'] = pd.to_datetime(self.data['OrderDate'])

    def key_metrics(self):
        total_revenue = self.data['Sales'].sum()
        total_profit = self.data['Profit'].sum()
        customer_count = self.data['CustomerID'].nunique()
        return total_revenue, total_profit, customer_count

    def sales_trend(self):
        monthly_sales = self.data.resample('M', on='OrderDate').sum()
        fig = px.line(monthly_sales, x=monthly_sales.index, y='Sales', title='Monthly Sales Trend')
        return fig

    def top_5_products_by_revenue(self, n=5):
        top_products = self.data.groupby('CustomerName').agg({'Sales': 'sum'}).nlargest(n, 'Sales')
        fig = px.bar(top_products, x=top_products.index, y='Sales', title='Top 5 Products by Revenue')
        return fig

    def revenue_share_by_region(self):
        region_sales = self.data.groupby('Region').agg({'Sales': 'sum'})
        fig = px.pie(region_sales, values='Sales', names=region_sales.index, title='Revenue Share by Region')
        return fig

    def profit_vs_cost(self):
        self.data['Cost'] = self.data['Sales'] - self.data['Profit']
        fig = px.bar(self.data, x='CustomerName', y=['Profit', 'Cost'], title='Profit vs Cost per Product')
        return fig

    def run(self):
        st.title('Business Intelligence Dashboard')
        revenue, profit, customer_count = self.key_metrics()
        st.metric('Total Revenue', f'${revenue:,.2f}')
        st.metric('Total Profit', f'${profit:,.2f}')
        st.metric('Customer Count', customer_count)

        st.plotly_chart(self.sales_trend())
        st.plotly_chart(self.top_5_products_by_revenue())
        st.plotly_chart(self.revenue_share_by_region())
        st.plotly_chart(self.profit_vs_cost())

# Usage Example
data = {
    'CustomerID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'CustomerName': ['Customer_1', 'Customer_2', 'Customer_3', 'Customer_4', 'Customer_5', 'Customer_6', 'Customer_7', 'Customer_8', 'Customer_9', 'Customer_10'],
    'Region': ['East', 'West', 'North', 'East', 'East', 'West', 'North', 'North', 'East', 'South'],
    'Sales': [3734, 4005, 5658, 2899, 8734, 2267, 2528, 4556, 4890, 9838],
    'Profit': [1062, 2884, -936, 2928, 2910, 1568, 367, 152, 1027, 1695],
    'Quantity': [14, 7, 9, 15, 15, 10, 13, 19, 7, 17],
    'Discount': [0.09, 0.09, 0.01, 0.18, 0.15, 0.02, 0.08, 0.27, 0.07, 0.04],
    'OrderDate': ['2023-01-01', '2023-01-08', '2023-01-15', '2023-01-22', '2023-01-29', '2023-02-05', '2023-02-12', '2023-02-19', '2023-02-26', '2023-03-05']
}

df = pd.DataFrame(data)
app = DashboardApp(df)
app.run()

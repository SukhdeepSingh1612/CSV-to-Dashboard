#!/usr/bin/env python
import sys
import warnings
import os
import pandas as pd
from datetime import datetime

from bi_dashboard_builder.crew import DashboardBuilderCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Load CSV dataset
csv_path = "data/sample_business_data.csv"
df = pd.read_csv(csv_path)

# Convert the first few rows to a markdown-style string for agent input
sample_data_preview = df.head(10).to_markdown(index=False)

requirements = f"""
Generate a Business Intelligence Dashboard using the following dataset:

Dataset Preview:
{sample_data_preview}

The dashboard should include:
- Key metrics like Total Revenue, Profit, and Customer Count
- Time-series sales trend over months
- Top 5 Products by Revenue
- Pie chart of revenue share by region
- Optional: Profit vs Cost per product as a bar chart

The output should be a Streamlit app using Plotly charts.
"""

module_name = "dashboard.py"
class_name = "DashboardApp"


def run():
    """
    Run the dashboard builder crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = DashboardBuilderCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()


# 📊 Dashboard Builder Crew

This project uses [CrewAI](https://github.com/joaomdmoura/crewAI) to automatically generate a Business Intelligence Dashboard from a CSV dataset.

## 🚀 Features

- Parses CSV input data
- Generates a Streamlit dashboard app
- Charts include:
  - 📈 Sales trend over time
  - 🥇 Top 5 products by revenue
  - 🧭 Revenue share by region (pie chart)
  - 📊 Profit vs. Cost per product (optional)
- Uses Plotly for visualizations

## 📂 Project Structure

```
.
├── data/
│   └── sample_business_data.csv
├── dashboard_builder/
│   └── crew.py              # Defines the Crew and its behavior
├── output/
│   └── dashboard.py         # Generated dashboard app
├── main.py                  # Main script to run the Crew
└── README.md                # This file
```

## 📦 Requirements

- Python 3.9–3.11
- CrewAI >= 0.25.2
- ChromaDB >= 0.4.13
- Streamlit
- Plotly
- pandas

You can install dependencies using `uv`:
```bash
uv pip install -r requirements.txt
```

## 🛠️ Usage

Run the crew to generate the dashboard:

```bash
python main.py
```

Once the dashboard is generated in the `output/` folder, launch it with:

```bash
streamlit run output/dashboard.py
```

## 🧠 Crew Details

The crew is defined in `dashboard_builder/crew.py` and is responsible for:

- Understanding the dataset and requirements
- Designing the layout and content of the dashboard
- Writing a `dashboard.py` file using Streamlit + Plotly

---

Created with 💡 using CrewAI.

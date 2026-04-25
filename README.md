## Sales Performance Analysis

Identifying revenue drivers and seasonal patterns to improve business decisions

---

## The Business Problem

Most businesses track sales data but fail to understand what actually drives revenue growth.

This leads to:
Over reliance on a small number of products
Uneven regional performance going unnoticed
Poor demand planning across seasons
This analysis identifies where revenue is generated, where it is lost, and what drives performance differences.

---

## Key Findings

| Finding | Business Implication |
|---|---|
| Burgers dominate total revenue | Revenue is heavily concentrated in one product category, creating dependency risk |
| Lisbon consistently outperforms all other cities | Strong regional imbalance suggests either demand differences or operational gaps |
| November shows the highest revenue spike | Clear seasonal trend. Demand planning should be focused ahead of Q4 |

- Revenue is highly concentrated in a small product group
- Regional performance varies significantly across cities
- Sales are predictably seasonal, with Q4 being the strongest period


**What does this mean** 
- Revenue is not evenly distributed across products or regions. Growth depends on optimizing a few high-impact areas rather than treating all segments equally.
 Improving performance depends on optimizing a few high-impact areas rather than treating all segments equally.
If unmanaged, dependency on a single product or region can create unstable revenue streams.

---

## Dataset

Transactional sales records containing:

| Column | Description |
|---|---|
| Order ID | Unique identifier per transaction |
| Date | Date of sale (used for monthly trend analysis) |
| Product | Item sold |
| Price | Unit price |
| Purchase Type | Sales category |
| Manager | Sales manager responsible |
| City | Location of transaction |
| Revenue | Total amount generated |



## Methodology
- Cleaned and standardized transactional data
- Extracted time based features (month, year)
- Aggregated performance by product, city, and time
- Visualized trends to identify patterns in revenue behavior

---

## Tools Used

• Python (Pandas, NumPy, Matplotlib)

---

## Visualizations

### Monthly Revenue Trend
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/4d7bc228-0d7d-4872-8146-46330ad461e8" />

### Top Products by Revenue
<img width="1500" height="800" alt="image" src="https://github.com/user-attachments/assets/f3b8bcb9-dc74-4a5d-9cb5-5ad6303eeb3a" />

---

## Project Structure

- sales-report/
- data/               # Raw dataset
- results/            # Output charts
- flow/               # Analysis modules
- main.py             # Run this to reproduce the full analysis
- requirements.txt    # Dependencies
- README.md

## How to Run

bash
- git clone https://github.com/HillaryIkhais/sales-report
- cd sales-report
- pip install -r requirements.txt
- python main.py

---

## What this analysis enables
- Identify products worth scaling
- Improve underperforming regions
- Plan inventory and marketing around demand cycles

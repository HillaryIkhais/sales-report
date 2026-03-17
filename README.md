## Sales Performance Analysis

> Identifying revenue stream and seasonal patterns to support smarter business decisions.

---

## The Business Problem

Many businesses track sales without knowing "why" their numbers go up or down. This project answers three questions any sales manager actually cares about:

- **Which products are carrying the business?** (And which ones aren't)
- **Which regions should get more resources?** (Based on actual performance)
- **When does revenue peak and why?** (To plan inventory and marketing around real demand)

---

## Key Findings

| Finding | Business Implication |
|---|---|
| Burgers dominate total revenue | One product category is driving a disproportionate share of income, that is, a concentration risk worth flagging to leadership |
| Lisbon consistently outperforms all other cities | Regional disparity suggests either market differences or management quality gaps worth investigating |
| November shows the highest revenue spike | Strong seasonality signal inventory and staffing should be scaled up ahead of Q4, not during it |

**So what does this mean?** A business acting on these findings could: double down on top products, replicate Lisbon's approach in underperforming regions, and start Q4 prep in September not November.

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



1. **Data Cleaning** Handled missing values, duplicates, and type conversions
2. **Feature Engineering** Extracted month/year from dates; computed revenue per transaction
3. **Aggregation** GroupBy operations across product, city, and time dimensions
4. **Visualization** Charts to surface patterns invisible in raw tables

---

## Tech Stack

• Python
• Pandas
• NumPy
• Matplotlib

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

## What's Next

- [ ] Correlation analysis - How does price sensitivity vary by region?
- [ ] Interactive dashboard (Power BI or Plotly Dash)
- [ ] Q4 revenue forecasting model
- [ ] Statistical significance testing on seasonal trends

---

## About

**I am Hillary Ikhais, a Data Analyst specializing in Python-based analysis and translating raw data into business decisions.**

 Open to freelance projects. [View more work on GitHub](https://github.com/HillaryIkhais)

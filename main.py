import pandas as pd
import numpy as np

from flow.clean import clean_data, get_data_summary
from flow.analyze import generate_insights
from flow.visualize import create_all_visualizations

#"_" * 20 is to print _ 20 times, to make it more readable
def main():
    print("SALES DATA ANALYSIS")
    main()

raw_data = pd.read_csv('data/Sales-Data-Analysis.csv')
print(f"Loaded data: {len(raw_data):,} rows")
    
# Clean data
cleaned_data = clean_data(raw_data)
print(f"Cleaned data: {len(cleaned_data):,} rows")

# Show data summary
print("\n Data Summary: ")
get_data_summary(cleaned_data)

# Generate Insights from analyze.py
print("\n Key Insights:")
insights = generate_insights(cleaned_data)
print(insights)

#Create visualizations from visualize.py
print("\n Visualizations Created: ")
create_all_visualizations(cleaned_data)

# Save cleaned data
output_path = 'data/clean_sales_data.csv'
cleaned_data.to_csv(output_path, index=False)
print(f"\n Cleaned data saved to: {output_path}")
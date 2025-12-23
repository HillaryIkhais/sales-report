import pandas as pd
import numpy as np

def top_performers(salesdata, column, top_n=5): 
    top_n = int(top_n) 
    return salesdata.groupby(column)['Revenue'].sum().sort_values(ascending=False).head(top_n) 
#sort_values(ascending=False sorts the values in descending order)

#Calculate top products by revenue
def rank_best_products(salesdata,top_n): 
    return top_performers(salesdata, 'Product', top_n) 

# Calculate total revenue by city
def rank_best_cities(salesdata, top_n):
    return top_performers(salesdata, 'City', top_n)

#Calculate top managers by revenue
def rank_best_managers(salesdata, top_n):
    return top_performers(salesdata, 'Manager', top_n)

#Calculate monthly revenue
def monthly_revenue(salesdata):
    return salesdata.groupby(['Year', 'Month'])['Revenue'].sum().sort_index()

#Calculate daily revenue, .groupby() is simply to group output by specified terms, in this case day of the week and revenue
def daily_revenue(salesdata):
    day_revenue = salesdata.groupby('DayOfWeek')['Revenue'].sum()

# day_order simply spcifies the order which the output is meant to be in
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                 "Friday", "Saturday", "Sunday"]

#.reindex() is to return the day_order command   
    return day_revenue.reindex(day_order, fill_value=0)

# generate a summary of key insights from the salesdata
def generate_insights(salesdata):
    insights = []
    
# Total revenue, .sum() adds the total revenue
    total_revenue = salesdata['Revenue'].sum()
#f string is a formatted string that allows variables, the $ is currency for total revenue, ',' is to add commas to the final value and 2f is to print as 2 decimal places
    insights.append(f"Total Revenue: ${total_revenue:,.2f}")
    
# Best product, .index() calls the name of the product and .values() calls the numerical salesdata, [0:] prints out the values till the specified end(n=3)
    top_products = rank_best_products(salesdata, top_n=5)
    insights.append("\nBest Products:")
#the for loop is to return more than one value
    for i in range(len(top_products)):
        name = top_products.index[i]
        revenue = top_products.values[i]
        insights.append(f"  {i+1}. {name} (${revenue:,.2f})")

# Best cities, explained in line 40
    top_cities = rank_best_cities(salesdata, top_n=5)
    insights.append("\nBest Cities:")
    for i in range(len(top_cities)):
        name = top_cities.index[i]
        revenue = top_cities.values[i]
        insights.append(f"  {i+1}. {name} (${revenue:,.2f})")

    top_managers = rank_best_managers(salesdata, top_n=5)
    insights.append("\nBest Managers:")
    for i in range(len(top_managers)):
        name = top_managers.index[i]
        revenue = top_managers.values[i]
        insights.append(f"  {i+1}. {name} (${revenue:,.2f})")

# Best day of week
    daily = daily_revenue(salesdata)
#DEBUGGING CODE
    #print(f"DEBUG: Type of daily: {type(daily)}")
    #if hasattr(daily, 'columns'):
    #print(f"DEBUG: Columns of daily: {daily.columns.tolist()}")
    #print(f"DEBUG: Type of daily Index: {type(daily.index)}")
    #print(f"DEBUG: Head of daily Index: {daily.index[:5].tolist()}")
 
# .max() returns the highest value, .idmax() returns the index where the value is (e.g Friday)
    daily = daily_revenue(salesdata)
    best_day = daily.idxmax()
    insights.append(f"\nBest Day: {best_day} (${daily[best_day]:,.2f})")
    
    return "\n".join(insights)
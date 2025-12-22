## salesdata CLEANING
import pandas as pd

def clean_data(salesdata):
    #to create a copy of the original
    salesdata = salesdata.copy()

    #remove duplicates
    salesdata = salesdata.drop_duplicates()
    
    # convert Date to datetime
    salesdata['Date'] = pd.to_datetime(salesdata['Date'], errors='coerce')
    
    salesdata['Year'] = salesdata['Date'].dt.year
    salesdata['Month'] = salesdata['Date'].dt.month_name()
    salesdata['Day'] = salesdata['Date'].dt.day
    salesdata['DayOfWeek'] = salesdata['Date'].dt.day_name()
    salesdata['Quarter'] = salesdata['Date'].dt.quarter
    
    # Calculate Revenue: Price × Quantity
    salesdata['Revenue'] = salesdata['Price'].fillna(0) * salesdata['Quantity'].fillna(0)

    #Calculate Tax
    salesdata['Revenue_with_Tax'] = salesdata['Revenue'] * 1.05

    #Clean text columns
    text_cols = ['Order ID', 'Date', 'Product', 'Price', 'Quantity', 'Purchase Type', 'Payment Method', 'Manager', 'City']
    for col in text_cols:
        if col in salesdata.columns:
            salesdata[col] = salesdata[col].astype(str).str.strip()
            salesdata[col] = salesdata[col].str.split().str.join(' ')
            salesdata[col] = salesdata[col].str.upper()
    return salesdata

def get_data_summary(salesdata):

    print("salesdata SUMMARY")

    print("\nMissing Values:")
    missing = salesdata.isnull().sum()
    if missing.sum() == 0:
        print("No missing values")
    else:
        print(missing[missing > 0])
    
    if 'Order ID' in salesdata.columns:
        duplicates = salesdata['Order ID'].duplicated().sum()
        print(f"\nDuplicate Order IDs: {duplicates}")
    
    print("\nRevenue Statistics:")
    if 'Revenue' in salesdata.columns:
        print(salesdata['Revenue'].describe())
    
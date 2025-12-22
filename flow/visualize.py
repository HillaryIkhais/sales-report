import matplotlib.pyplot as plt


plt.style.use('seaborn-v0_8-whitegrid')

# Custom color palette

#barh is to plot a horizontal graph
def plot_bar(salesdata, title, xlabel="Revenue", ylabel=None):
    plt.figure(figsize=(15, 8))
    salesdata.plot(kind='barh', color = '#1F2A44')
    plt.title(title, fontsize=16, fontweight='bold', color = '#2E2E2E')
    plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"results/{title}.png")
    plt.close()
    plt.show()

#plt.tight_layout is to make sure all values are revealed and not hidden
def plot_top_products(salesdata):
    from flow.analyze import rank_best_products
    
    salesdata = rank_best_products(salesdata, 5)
    plot_bar(salesdata, f"Top 5 Products by Revenue", "Revenue ($)", "Product")
    plt.show()

def plot_top_cities(salesdata):
    from flow.analyze import rank_best_cities
    
    salesdata = rank_best_cities(salesdata, 5)
    plot_bar(salesdata, f"Top 5 Cities by Revenue", "Revenue ($)", "City")
    plt.show()

def plot_top_managers(salesdata):
    from flow.analyze import rank_best_managers
    
    salesdata = rank_best_managers(salesdata, 5)
    plot_bar(salesdata, f"Top 5 Managers by Revenue", "Revenue ($)", "Manager")
    plt.show()

def plot_monthly_trend(salesdata):
    from flow.analyze import monthly_revenue
    
    month_revenue = monthly_revenue(salesdata)
    
    plt.figure(figsize=(12, 6))
    month_revenue.plot(marker='*', linewidth=2, color = '#1F2A44')
    plt.title("Monthly Revenue Trend", fontsize=16, fontweight='bold', color = '#2E2E2E')
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("results/Monthly Revenue.png")
    plt.show()

def plot_revenue_by_day(salesdata):
    from flow.analyze import daily_revenue
    
    day_revenue = daily_revenue(salesdata)
    
    plt.figure(figsize=(10, 6))
    day_revenue.plot(marker='*', linewidth=2, color = '#1F2A44')
    plt.title("Revenue by Day of Week", fontsize=16, fontweight='bold', color = '#2E2E2E')
    plt.xlabel("Day")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)  # Rotate labels so they don't overlap
    plt.tight_layout()
    plt.savefig("results/Daily Revenue.png")
    plt.show()


def create_all_visualizations(salesdata):
    print("\n1. Top Products")
    plot_top_products(salesdata)
    
    print("\n2. Top Cities")
    plot_top_cities(salesdata)
    
    print("\n3. Top Managers")
    plot_top_managers(salesdata)
    
    print("\n4. Monthly Trend")
    plot_monthly_trend(salesdata)
    
    print("\n5. Revenue by Day of Week")
    plot_revenue_by_day(salesdata)
    
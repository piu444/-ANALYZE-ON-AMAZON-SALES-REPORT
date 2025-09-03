import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Amazon_Sale_Report_Cleaned_Interpolated.csv')

# # most common product plot
# top_product = df['Category'].value_counts().head(15)
# plt.figure(figsize=(10, 6))
# top_product.plot(kind='bar', color = 'lightgreen', edgecolor='black')
# plt.title('Top 15 Most Common Products')
# plt.xlabel('Product Category')
# plt.ylabel('Count')
# plt.xticks(rotation=-90)
# plt.tight_layout()
# plt.show()
# plt.savefig('most_common_products.png')

# # most common order ID plot
# top_order = df['Order ID'].value_counts().head(15)
# plt.figure(figsize=(10, 6))
# top_order.plot(kind='bar', color = 'skyblue', edgecolor='black')
# plt.title('Top 15 Most Common Order IDs')
# plt.xlabel('Order ID')
# plt.ylabel('Count')
# plt.xticks(rotation=-90)
# plt.tight_layout()
# plt.show()
# plt.savefig('most_common_order_ids.png')

# # sales trend over time plot
# df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')  # Use format for day-month-year

# # Group by date and count orders for each day
# daily_sales = df.groupby(df['Date'].dt.date).size()

# # Alternatively, group by month for a broader trend
# monthly_sales = df.groupby(df['Date'].dt.to_period('M')).size()

# plt.figure(figsize=(12, 6))
# daily_sales.plot(kind='line', marker='o', color='black',   )
# plt.title('Sales Trend Over Time')
# plt.xlabel('Order Date')
# plt.ylabel('Number of Orders')
# plt.xticks(rotation=45)
# plt.gca().set_facecolor('lightgreen')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.savefig('sales_trend_over_time.png')
# plt.show()

# # popilar size plot
# top_size = df['Size'].value_counts().head(8)
# plt.figure(figsize=(8, 5))
# top_size.plot(kind='bar', color = 'orange', edgecolor='black')
# plt.title('Top 8 Most Common Sizes')
# plt.xlabel('Size')
# plt.ylabel('Count')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('most_common_sizes.png')
# plt.show()


# # Group by customer and sum their sales

# top10_customers = df.groupby('Order ID')['Amount'].sum().sort_values(ascending=False).head(10)

# plt.figure(figsize=(12,6))
# top10_customers.plot(kind='bar', color='orange', edgecolor='black')
# plt.title("Top 10 Customers by Sales Contribution")
# plt.ylabel("Total Sales (₹)")
# plt.xlabel("Customer Name")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()

# # tpo 10 states by sales
# top_states = df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(10)
# print("Top 10 states by sales:")
# print(top_states)
# plt.figure(figsize=(12,6))
# top_states.plot(kind='bar', color='lightgreen', edgecolor='black')
# plt.title("Top 10 States by Sales")
# plt.ylabel("Total Sales (₹)")
# plt.xlabel("State")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()
# plt.savefig('top_10_states_by_sales.png')

# top 10 cities by sales pie chart
top_cities = df.groupby('ship-city')['Amount'].sum().sort_values(ascending=False).head(10)
print("Top 10 cities by sales:")
print(top_cities)
plt.figure(figsize=(8,8))
top_cities.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Top 10 Cities by Sales")
plt.ylabel("")  # Hide y-label for pie chart
plt.tight_layout()
plt.show()
plt.savefig('top_10_cities_by_sales.png')

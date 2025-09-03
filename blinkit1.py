import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('Blinkit_data.csv')
print(df.head(10))
print("the size of data is: ", df.shape)
print(df.info())

print(df['Item Fat Content'].unique())
df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat','low fat': 'Low Fat' ,'reg': 'Regular'})
print(df['Item Fat Content'].unique())

# for total sales 
total_sales = print(df['Sales'].sum())
avg_sales = print(df['Sales'].mean())
total_item_sold = print(df['Item Identifier'].count())

sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()
sales_by_fat.plot(kind='bar', color=['blue', 'orange'])
plt.title('Total Sales by Item Fat Content')
plt.xlabel('Item Fat Content')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.show()


# for pie chart
sales_by_fat.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['blue', 'orange'])
plt.title('Sales Distribution by Item Fat Content')
plt.ylabel('')
plt.show()

# total sales by item types
sales_by_type = df.groupby('Item Type')['Sales'].sum()
bars = sales_by_type.plot(kind='bar', color='green')
plt.title('Total Sales by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.xticks(rotation=-90)
for bar in bars.containers[0]:
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height(),
             f'{bar.get_height():.0f}',
             ha='center', va='bottom')
    plt.tight_layout()
plt.show()

# fat content by outlet by total sales
group=fat_outlet_sales = df.groupby(['Item Fat Content', 'Outlet Identifier'])['Sales'].sum().unstack()
group = group[group.index.isin(['Low Fat', 'Regular'])]  # Filter for Low Fat and Regular
fat_outlet_sales.plot(kind='bar', stacked=True, color=['blue', 'orange'])
plt.title('Total Sales by Item Fat Content and Outlet')
plt.xlabel('Item Fat Content')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.show()

# total sales by outlet establishment year
sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

figure, ax = plt.subplots(figsize=(10, 6))
sales_by_year.plot(kind='bar', color='purple', ax=ax)
plt.title('Total Sales by Outlet Establishment Year')
plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
for bar in ax.containers[0]:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{bar.get_height():.0f}',
            ha='center', va='bottom')
plt.tight_layout()
plt.show()

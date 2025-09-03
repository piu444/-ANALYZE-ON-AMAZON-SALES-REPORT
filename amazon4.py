import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Amazon_Sale_Report_Cleaned_Interpolated.csv')

# total cancled orders 
total_canceled_orders = df[df['Status'] == 'Cancelled']['Order ID'].nunique()
print(f"Total canceled orders: {total_canceled_orders}")

# most common cancelled product
most_common_canceled_product = df[df['Status'] == 'Cancelled']['Category'].value_counts().idxmax()
canceled_product_count = df[df['Status'] == 'Cancelled']['Category'].value_counts().max()
print(f"Most common canceled product: {most_common_canceled_product} with {canceled_product_count} occurrences.")

# most common cancelled size 
size = df[df['Status'] == 'Cancelled']['Size'].value_counts().idxmax()
size_count = df[df['Status'] == 'Cancelled']['Size'].value_counts().max()
print(f"Most common cancelled size: {size} with {size_count} occurrences.")

cancel_df = df[df['Status'].str.contains('cancel', case=False, )]
if not cancel_df.empty:
    size = cancel_df['Size'].value_counts().idxmax()
    size_count = cancel_df['Size'].value_counts().max()
    print(f"Most common cancelled size (case insensitive): {size} with {size_count} occurrences.")
else:
    print("No cancelled orders found.")


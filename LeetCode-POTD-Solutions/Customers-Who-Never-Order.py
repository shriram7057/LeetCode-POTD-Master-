import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Left join customers with orders on 'id' and 'customerId'
    merged = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    # Filter customers where 'customerId' from orders is null (i.e., never ordered)
    never_ordered = merged[merged['customerId'].isna()]
    # Select and rename the result column
    result = never_ordered[['name']].rename(columns={'name': 'Customers'})
    return result

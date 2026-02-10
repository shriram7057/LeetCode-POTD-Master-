import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = (
        orders.groupby('customer_number')['order_number']
        .count()
        .reset_index(name='order_count')
        .sort_values('order_count', ascending=False)
        .head(1)[['customer_number']]
    )
    return result

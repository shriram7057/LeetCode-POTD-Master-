import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Use melt() to unpivot the table
    result = products.melt(
        id_vars=['product_id'],
        var_name='store',
        value_name='price'
    )

    # Remove rows where price is null (NaN)
    result = result.dropna(subset=['price'])

    return result

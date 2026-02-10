import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_years = (
        sales.groupby("product_id")["year"]
             .min()
             .reset_index()
             .rename(columns={"year": "first_year"})
    )

    merged = sales.merge(first_years, on="product_id")
    result = merged[merged["year"] == merged["first_year"]]

    return result[["product_id", "first_year", "quantity", "price"]]

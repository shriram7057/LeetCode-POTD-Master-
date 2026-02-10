import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define salary category conditions
    low = (accounts['income'] < 20000).sum()
    average = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high = (accounts['income'] > 50000).sum()
    
    # Create output DataFrame
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low, average, high]
    })
    
    return result

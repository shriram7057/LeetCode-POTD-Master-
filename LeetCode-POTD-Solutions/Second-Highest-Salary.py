import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate salaries and sort in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    # Check if at least 2 salaries exist
    if len(unique_salaries) >= 2:
        second_salary = float(unique_salaries.iloc[1])   # 2nd highest
    else:
        second_salary = pd.NA   # Return null if not exist
    
    # Return result with required column name
    return pd.DataFrame({'SecondHighestSalary': [second_salary]})

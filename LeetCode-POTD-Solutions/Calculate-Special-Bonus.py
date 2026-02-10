import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] if row['employee_id'] % 2 != 0 and row['name'][0] != 'M' else 0,
        axis=1
    )
    result = employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    return result

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee with department on departmentId
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))

    # Find the maximum salary for each department
    max_salaries = merged.groupby('name_dept')['salary'].max().reset_index()

    # Join back to get employee names who have that salary
    result = merged.merge(max_salaries, left_on=['name_dept', 'salary'], right_on=['name_dept', 'salary'])

    # Select required columns and rename as per LeetCode output
    result = result[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    return result

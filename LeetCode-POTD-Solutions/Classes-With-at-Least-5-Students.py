import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (
        courses.groupby('class')['student']
        .nunique()                         # count distinct students per class
        .reset_index(name='student_count')  # rename count column
    )
    result = result[result['student_count'] >= 5][['class']]  # keep only classes with >= 5
    return result

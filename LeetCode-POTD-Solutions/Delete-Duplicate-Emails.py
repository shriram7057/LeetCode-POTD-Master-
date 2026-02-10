import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by id to keep the smallest id for each email
    person.sort_values(by='id', inplace=True)

    # Drop duplicates in-place, keeping the first occurrence
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)

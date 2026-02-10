import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Rank scores in descending order
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)

    # Sort by rank for output
    result = scores.sort_values(by='rank')[['score', 'rank']]

    return result

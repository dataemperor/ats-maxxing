import pandas as pd
from pathlib import Path


def ats_scanner(input_string):
    """
    Compares the tokenized string input to a list of keywords
    If a token is equal to a keyword, the keyword count is incremented
        keyword is added to used_keywords

    TODO: implement this feature for different file types
    """
    keyword_count = 0
    used_keywords = set()

    lowercase_input_string = input_string.lower()
    tokens = lowercase_input_string.split()

    current_path = Path(__file__)
    keyword_csv_path = current_path.parent.parent / 'data' / \
        'processed' / 'common-keywords-processed.csv'

    df = pd.read_csv(keyword_csv_path)
    keywords = df['Keyword'].tolist()

    for keyword in keywords:
        if keyword.lower() in tokens and keyword.lower() not in used_keywords:
            keyword_count += 1
            used_keywords.add(keyword.lower())

    return keyword_count


def ats_score(keyword_count):
    """
    Returns a message along with the keyword count
    """
    if keyword_count == 1:
        return ("There is only ONE keyword in your text!\
        Please try adding more!")
    elif keyword_count <= 5:
        return (f"Low keyword count! There are only {keyword_count}\
        keywords in your text! Try adding more!")
    elif keyword_count >= 5:
        return (f"High keyword count! There are {keyword_count}\
        keywords in your text! That should be enough to get noticed.")

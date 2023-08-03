import re
import pandas as pd

def split_on_conj_preposition_article(text):
    # Define the regular expression pattern
    pattern = r'\b(?:but|or|for|in|of|the|a|an|: |, |toward|and|about|trained|using)\b'

    # Use re.split() to split the string based on the pattern
    result = re.split(pattern, text, flags=re.IGNORECASE)

    # Filter out empty strings from the result
    result = [word.strip() for word in result if word.strip()]

    return result

df=pd.read_csv('google_scholar.csv')
i = 2016
titles = df.loc[df['year']==i].title
file = open(f'F:\\Google Scholar Scraping\keywords\\keywords_{i}.txt','a')
for title in titles:
    output = split_on_conj_preposition_article(title)
    file.write(f'>>> {title} : {output}\n')
file.close()
    
# Example usage
# input_string = "Developing residential wireless sensor networks for ECG healthcare monitoring"
# output = split_on_conj_preposition_article(input_string)
# print(">>>",output)

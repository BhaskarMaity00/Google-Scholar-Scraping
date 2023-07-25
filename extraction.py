import pandas as pd
import numpy as np
import re
import string

df=pd.read_csv('google_scholar.csv')
max_year=df['year'].max()
min_year=df['year'].min()

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from stop_words import get_stop_words

from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = PorterStemmer()
stop_words = get_stop_words('en')
nltk_words = stopwords.words('english')
stop_words.extend(nltk_words)

def tokenizer(keyword):
    return [stemmer.stem(w) for w in re.sub('['+string.punctuation+']', '', keyword).split()]

data=[]
for i in range(max_year,min_year-1,-1):
    titles = df.loc[df['year']==i].title
    for words in titles:
        keywords=[]
        keywords.append(words)
        tfidf = TfidfVectorizer(tokenizer=tokenizer,stop_words=stop_words)
        x=tfidf.fit_transform(keywords).toarray()
        y=list(tfidf.get_feature_names_out())
        data.append({
                    "Title":words,
                    "Year":i,
                    "Keywords":y})
pd.DataFrame(data).to_csv("Keyword_list.csv",index=False)
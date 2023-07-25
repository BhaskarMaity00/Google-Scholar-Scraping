import pandas as pd
import numpy as np
import re
import string

df=pd.read_csv('google_scholar.csv')

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from stop_words import get_stop_words

from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn import cluster

stemmer = PorterStemmer()
stop_words = get_stop_words('en')
nltk_words = stopwords.words('english')
stop_words.extend(nltk_words)

def tokenizer(keyword):
    return [stemmer.stem(w) for w in re.sub('['+string.punctuation+']', '', keyword).split()]

data=[]
titles = df.loc[df['year']==2022].authors.str.upper()
for words in titles:
    keywords=[]
    keywords.append(words)
    tfidf = TfidfVectorizer(tokenizer=tokenizer,stop_words=stop_words)
    x=tfidf.fit_transform(keywords).toarray()
    y=list(tfidf.get_feature_names_out())
    data.append({
                 "Title":words,
                 "Year":df.loc[df['title']==words,"year"].iloc[0],
                 "Keywords":y})
pd.DataFrame(data).to_csv("Keyword_list.csv",index=False)
# x = pd.DataFrame(tfidf.fit_transform(keywords).toarray(),columns=tfidf.get_feature_names_out())
# print(x)
# c = cluster.AffinityPropagation()
# y = c.fit_predict(x)
# x['pred'] = c.fit_predict(x)
# x['title']=keywords
# x=x.sort_values("pred",ascending=True)


    
    
    
# pd.DataFrame(data=df1).to_csv(f"cluster.csv",index=False)
# pd.DataFrame(data=df1[['pred','title']]).to_csv(f"cluster.csv",index=False)
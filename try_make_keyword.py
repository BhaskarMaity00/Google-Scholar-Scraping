import pandas as pd
import keyword_making

df=pd.read_csv('google_scholar.csv')
i = 2022
titles = df.loc[df['year']==i].title.str.upper()

keywords = []
for title in titles:
    words = keyword_making.main(title)
    keywords.extend(y for y in words if y not in keywords)
    
file = open(f'keywords{i}.txt','w')
for keyword in keywords:
	file.write(keyword+" ")
file.close()
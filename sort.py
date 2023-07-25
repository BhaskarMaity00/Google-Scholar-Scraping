# import pandas as pd
# import csv
# df = pd.read_csv('google_scholar.csv')
# cx = df.sort_values("year",ascending=False)
# pd.DataFrame(data=cx).to_csv(f"google_scholar_sort.csv", index=False)
import re
my="hello world,my:name"
lis=re.split(r',|:| ',my)
print(lis)
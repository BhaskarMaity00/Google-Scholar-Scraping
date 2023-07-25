import wn
en = wn.Wordnet('own-en:1.0.0')
ss = en.synsets('heart')
for i in ss:
    print(i,"-->",i.lemmas())

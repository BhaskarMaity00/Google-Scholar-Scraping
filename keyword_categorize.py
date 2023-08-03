import gensim.downloader as api

# Load the pre-trained Word2Vec model
model = api.load("word2vec-google-news-300")

def categorize_word(word):
    # Check if the word is in the vocabulary
    if word in model.key_to_index:
        # Get the word embedding vector
        word_vector = model[word]
        
        # Perform word similarity to find the most similar category words
        categories = model.most_similar(positive=[word_vector])
        category_words = [cat[0] for cat in categories]
        return category_words
    else:
        return 'unknown'


file = open('keywords2022.txt','r')
keywords = file.read().split(" ")
for word in keywords:
    category_words = categorize_word(word)
    with open("keywordcategorise2022.txt", 'a') as f:
        f.write(f'{word}: {category_words} \n')
        
# category_words = categorize_word(keywords[0])
# print(f'{keywords[0]}: {category_words} \n')

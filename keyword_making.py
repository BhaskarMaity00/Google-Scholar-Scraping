import spacy
from collections import Counter

def extract_keywords(sentence):
    # Load the SpaCy language model
    nlp = spacy.load("en_core_web_sm")

    # Process the sentence
    doc = nlp(sentence)

    # Filter, lemmatize, and remove stop words
    filtered_words = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and token.is_alpha
    ]

    # Count word frequencies
    word_freq = Counter(filtered_words)

    # Get the most common words (keywords)
    keywords = [word for word,freq in word_freq.most_common()]

    return keywords

def main(title):
    keywords = extract_keywords(title)
    return keywords

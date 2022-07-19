from nltk.stem import WordNetLemmatizer
import re
import numpy as np

def preprocess_text_sklearn(textDf, vectorizer, tfidfconverter):
    sent = textDf[textDf["sent or rec"] == "sent"]
    X = list(sent.message)
    documents = []
    stemmer = WordNetLemmatizer()
    for sen in X:
        # print("sentence: ", sen)
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(sen))
        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)
        # Converting to Lowercase
        document = document.lower()
        # Lemmatization
        document = document.split()
        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
        documents.append(document)

    X_vectorized = vectorizer.transform(documents).toarray()
    X_converted = tfidfconverter.transform(X_vectorized).toarray()
    # print(np.shape(X_converted))
    return X_converted


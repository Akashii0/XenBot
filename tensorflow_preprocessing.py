import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Prepare the text data
#text = ["hello how are you", "I am fine", "how about you", "bye bye", "thank you"]
text = []
# Tokenize the words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text)
tokenized_words = tokenizer.texts_to_sequences(text)

# Pad sequences to the same length
padded_sequences = pad_sequences(tokenized_words, padding='post')

# Stem the words using Porter Stemmer
stemmed_words = [["".join(tf.keras.preprocessing.text.text_to_word_sequence(sentence, split=' ')) for sentence in text]]

# Use the NLTK Porter Stemmer
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
stemmed_words = [[stemmer.stem(word) for word in sentence.split()] for sentence in tokenizer.texts_to_sequences(stemmed_words[0])]

# Print the stemmed words
print(stemmed_words)

#Print the tokenized and padded sequences
print(padded_sequences)
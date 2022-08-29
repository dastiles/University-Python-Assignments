from nltk.stem import PorterStemmer , WordNetLemmatizer
import nltk

sentence = 'i want to tokenize this sentence into smaller words'

tokens = nltk.tokenize.word_tokenize(sentence)

print(tokens)



stemer = PorterStemmer()
lem = WordNetLemmatizer()

words = ['run', 'running', 'runs', 'runned','ran']
words2 = ['run', 'running', 'runs', 'runned','ran']

words = [stemer.stem(word) for word in words]

words2 = [lem.lemmatize(word) for word in words2]

print(words)
print(words)
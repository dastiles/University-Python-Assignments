from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.util import bigrams,trigrams,ngrams
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


text = "Each personal computer has a microprocessor that manages the computer's arithmetical, logical, and control activities.Each family of processors has its own set of instructions for handling various operations such as getting input from keyboard, displaying information on screen, and performing various other jobs. These set of instructions are called 'machine language instructions'.A processor understands only machine language instructions, which are strings of 1's and 0's. However, machine language is too obscure and complex for using in software development. So, the low-level assembly language is designed for a specific family of processors that represents various instructions in symbolic code and a more understandable form."

tokens = word_tokenize(text)

# bigrams list
# print(list(bigrams(tokens)))

# trigram
# print(list(trigrams(tokens)))

# ngrams
# print(list(ngrams(tokens,5)))

# fdist = FreqDist()

# for word in tokens:
#     fdist[word.lower()]++1
#     print(fdist)

stemmer = PorterStemmer()

# for word in tokens:
#     print(f'{word} => {stemmer.stem(word)}')

print(stopwords)
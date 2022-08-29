
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
# documents = [
#     'i like nlp?',
#     'i am eploring nlp',
#     "i am a beginner in nlp",
#     'i want to learn nlp',
#     'i like advanced nlp',
# ]
documents = ['with', 'have', 'chickenpox']
random_words = "had have  chickenpox"

words = nltk.word_tokenize(random_words)
documents =  words + documents
# print(documents)
tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# print(tfidf_matrix.shape)

# #compute similarity for the first sentence with the rest of the sentences
# summin = cosine_similarity(tfidf_matrix[0:len(words)], tfidf_matrix[len(words):])
# summin = sum([sum(i) for i in summin])
# print(summin)
# print(max([1,3,4,55,7]))

def cosine_sim(text1, text2):
    tfidf = tfidf_vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


print(cosine_sim('i have monkeypox', 'monkeypox'))
print(cosine_sim('a little bird', 'a little bird chirps'))
print(cosine_sim('a little bird', 'a big dog barks'))

# def find_max_similarity(similarity_responces : dict) -> str:
#    max_similarity = 0
#    suitable_response = ''
#    for res, similarity in similarity_responces.items():
#       if similarity > max_similarity:
#          max_similarity = similarity
#          suitable_response = res
#          print(f"{res} : {similarity} is the highest")
#    return suitable_response
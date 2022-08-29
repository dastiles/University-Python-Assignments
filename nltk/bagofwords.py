from sklearn.feature_extraction.text import CountVectorizer

# create a model
from sklearn import svm
class Category:
    BOOKS = 'BOOKS'
    CLOTHING = 'CLOTHING'
train_x = ['i love the book', 'this is a great book', 'this fit is great', 'i love the shoes']

train_y = [Category.BOOKS,Category.BOOKS,Category.CLOTHING,Category.CLOTHING]

vectorizer = CountVectorizer(stop_words=True)
train_x_vectors = vectorizer.fit_transform(train_x)

print(train_x_vectors)
print(vectorizer.get_feature_names_out())
print(train_x_vectors.toarray())


# model building 
clf_svm = svm.SVC(kernel = 'linear')
clf_svm.fit(train_x_vectors,train_y)

test_x = vectorizer.transform(['i like the book'])
print(clf_svm.predict(test_x))


from sklearn.datasets import load_iris
iris=load_iris()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
iris.data, iris.target, test_size = .25)


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

print(" Accuracy=",clf.score(X_test, y_test))

print(clf.predict(X_test))
prediction=clf.predict(X_test)
print("Test data :")
print(y_test)

a=prediction-y_test
print("Result is ")
print(a)
print('Total no of samples misclassied =', sum(abs(a)))



import random




class ScrappyKNN():
    def fit(self,X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self,X_test):
        predictions = []
        for row in X_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = 1
        return self.y_train[best_index]


from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

from sklearn import tree
my_classifier = ScrappyKNN()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# import numpy as np
# from sklearn.datasets import load_iris
# from sklearn import tree
#
# iris = load_iris()
# test_idx = [0,50,100]
#
# # training data
# train_target = np.delete(iris.target, test_idx)
# train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
# test_target = iris.target[test_idx]
# test_data = iris.data[test_idx]
#
# clf = tree.DecisionTreeClassifier()
# clf.fit(train_data, train_target)
#
# print(test_target)
# print(clf.predict(test_data))
#
# # visualization code
# from sklearn.externals.six import StringIO
# import pydotplus
# dot_data=StringIO()
# tree.export_graphviz(clf,
#                      out_file=dot_data,
#                      feature_names=iris.feature_names,
#                      class_names=iris.target_names,
#                      filled=True, rounded=True,
#                      impurity=False)
#
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("iris.pdf")


# print(iris.feature_names)
# print(iris.target_names)
# print(iris.data[0])
# print(iris.target[0])



# this is the very first program that the Google course of machine learning had me do.
# I can manipulate the training data and the features in order to predict things
# from sklearn import tree
# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# labels = ["apple", "apple", "orange", "orange"]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print(clf.predict([[150, 0]]))

# from sklearn import tree
# features = [[5, 1], [4, 1], [1, 0], [2, 0]]
# labels = ["Developer", "Developer", "non-dev", "non-dev"]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print(clf.predict([[1, 1]]))




# import numpy as np
# import matplotlib.pyplot as plt
#
# greyhounds = 500
# labs = 500
#
# grey_height = 28 + 4 * np.random.randn(greyhounds)
# lab_height = 24 + 4 * np.random.randn(labs)
#
# plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
# plt.show()

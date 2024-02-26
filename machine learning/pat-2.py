from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
df = load_iris()
X = df.data
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=84)
# Naive Bayes
modelNb = GaussianNB()
modelNb.fit(X_train, y_train)
GaussianNB()
gauss_pred = modelNb.predict(X_test)
accuracy_naive = accuracy_score(y_test, gauss_pred)
print("Naive Bayes Accuracy: ", accuracy_naive)
# Multi Layer Perceptron
modelMlb = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=10000, activation='relu', random_state=73)
modelMlb.fit(X_train, y_train)
mlp_pred = modelMlb.predict(X_test)
accuracy_mlp = accuracy_score(y_test, mlp_pred)
print("MLP Accuracy: ", accuracy_mlp)
# Plot
classifiers = ['Naive Bayes', 'MLPClassifier']
accuracies = [accuracy_naive, accuracy_mlp]
plt.bar(classifiers, accuracies, color=['red', 'green'])
plt.xlabel('Classification Techniques')
plt.ylabel('Accuracy')
plt.title('Accuracy of Classification Techniques on Iris Dataset')
plt.ylim(0, 1)
plt.show()
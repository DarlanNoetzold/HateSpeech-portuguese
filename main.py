import pandas as pd
import numpy as np
import TextProcessor as prtxt
from sklearn.model_selection import cross_validate
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

TOTAL_KFOLDS = 10

kfolds = [i+1 for i in range(TOTAL_KFOLDS)]

metrics = ['accuracy', 'balanced_accuracy', 'roc_auc']
label_metrics = ['Acurácia', 'Acurácia Balanceada', 'Área sobre curva ROC']

names = ['Logistic Regression', 'Multinomial Naive Bayes',
         'Linear SVC (SVM)']
classifiers = [LogisticRegression(), MultinomialNB(), LinearSVC()]

proc = prtxt.TextProcessor()

data = pd.read_csv("base/base_dados.csv", encoding = 'utf-8')
originalText = data['frase']
marcs = data['valor']
textVectorization = proc.processar(originalText)
X = np.array(textVectorization)
Y = np.array(marcs.tolist())

x_train, x_valid, y_train, y_valid = train_test_split(X, Y, test_size=0.2, random_state=0)

results = []

results_tests_metrics = {}
results_validation = {}

for i in range(len(classifiers)):
    scores = cross_validate(classifiers[i], x_train, y_train, cv=TOTAL_KFOLDS, scoring=metrics)
    print("Scores: ")
    print(scores)
    results_tests_metrics[names[i]] = scores
print(results_tests_metrics)

for i in range(len(classifiers)):
    classifiers[i].fit(x_train, y_train)
    results = classifiers[i].predict(x_valid)
    accuracy = accuracy_score(y_valid, results)
    print("Results.: ")
    print(results)
    results_validation[names[i]] = accuracy
print(results_validation)

pickle.dump(classifiers, open('model/model_hate.pkl', 'wb'))
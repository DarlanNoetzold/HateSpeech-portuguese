import pandas as pd
import numpy as np
import TextTokenizer as trtxt
import TextProcessor as prtxt
from sklearn.model_selection import cross_validate
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import Grafics as grf

TOTAL_KFOLDS = 10

kfolds = [i+1 for i in range(TOTAL_KFOLDS)]

metrics = ['accuracy', 'balanced_accuracy', 'roc_auc']
label_metrics = ['Acurácia', 'Acurácia Balanceada', 'Área sobre curva ROC']

names = ['Logistic Regression', 'Multinomial Naive Bayes',
         'Linear SVC (SVM)']
classifiers = [LogisticRegression(), MultinomialNB(), LinearSVC()]

proc = trtxt.TextProcessor('pt')

preprocessed_data = prtxt.init()

originalText = preprocessed_data['frase']
marcs = preprocessed_data['valor']
fraseVectorization = proc.process(originalText)

X = np.array(fraseVectorization)
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

#Exibe uma imagem de um gráfico representando cada uma das métricas de avaliação empregadas.
for i in range(len(metrics)):
    res_mets = []
    for chave, valor in results_tests_metrics.items():
        res_mets.append(valor['test_' + metrics[i]])
    grf.mostrarGraficoLinhas(res_mets[0], res_mets[1], res_mets[2], kfolds,
                             [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], "Número do 'fold' (n)", label_metrics[i])

#Gera o gráfico dos tempos de fit time, ou seja, o tempo para realização de fit em cada classificador.
for i in range(len(classifiers)):
    t_fit_time = []
    for valor in results_tests_metrics.values():
        t_fit_time.append(valor['fit_time'])
    grf.mostrarGraficoLinhas(t_fit_time[0], t_fit_time[1], t_fit_time[2], kfolds,
                             [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5],
                             "Número do 'fold' (n)", "Fit Time (s)")

#Gera o gráfico de acurácia da previsão (predict) de cada classificador.
accs = []
for i in range(len(classifiers)):
    acc = results_validation.get(names[i])
    accs.append(acc)
grf.mostrarGraficoBarras(names, accs, "Acurácia (na Validação)")
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:26:53 2021

@author: Sabri
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                    iris_dataset['target'], 
                                                    random_state = 10)

clf = DecisionTreeClassifier()

#Lo entreno con los datos de entrenamiento
clf.fit(X_train, y_train)


#Predecir una flor
#Predecir la clase de una flor según sus cuatro medidas
X_new = np.array([[5, 2.9, 1, 0.2]])

plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

prediction = clf.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:", 
      iris_dataset['target_names'][prediction])

#Evaluación del modelo usando el 25% de los datos etiquetados
y_pred = clf.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score:{:.2f}".format(clf.score(X_test, y_test)) )



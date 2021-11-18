# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 18:06:23 2021

@author: Sabri
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                    iris_dataset['target'],
                                                    random_state = 0)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

#Creo una instancia de clase KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 1)

#La entrenamos con los datos de entrenamiento
knn.fit(X_train, y_train)

#Predecir una flor
#Predecir la clase de una nueva flor según sus cuatro medidas
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)

plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:", 
      iris_dataset['target_names'][prediction])

#Evaluación del modelo usando el 25% de los datos etiquetados
y_pred = knn.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

#para medir el éxito de la predicción
print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

#O usando el método score
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))




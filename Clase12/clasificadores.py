# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:49:55 2021

@author: Sabri
"""

import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


iris_dataset = load_iris()

#Creo las instancias de objeto de los clasificadores
knn = KNeighborsClassifier(n_neighbors = 1) 
clf = DecisionTreeClassifier()
clf_rf = RandomForestClassifier(max_depth = 2)


scores_neighbor = np.array([])
scores_tree = np.array([])
scores_random_forest = np.array([])
for i in range(100):
    #Separo los datos para entrenar y los datos para evaluar
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                    iris_dataset['target'])
    #Entreno los modelos
    knn.fit(X_train, y_train)
    clf.fit(X_train, y_train)
    clf_rf.fit(X_train, y_train)
    
    #Calculo los score de cada clasificador
    score_neighbor = knn.score(X_test, y_test)
    score_tree = clf.score(X_test, y_test)
    score_random_forest = clf_rf.score(X_test, y_test)
    
    #Agrego el score al array de scores
    scores_neighbor = np.append(scores_neighbor, score_neighbor)
    scores_tree = np.append(scores_tree, score_tree)
    scores_random_forest = np.append(scores_random_forest, score_random_forest)
    
print("El promedio de los scores usando KNeighbors es:{:.3f}"
      .format(np.mean(scores_neighbor)))
print("El promedio de los scores usando DecisionTree es {:.3f}"
      .format(np.mean(scores_tree)))
print("El promedio de los scores usando RandomForest es {:.3f}"
      .format(np.mean(scores_random_forest)))

    
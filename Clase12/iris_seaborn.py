# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:54:25 2021

@author: Sabri
"""

from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd

iris_dataset = load_iris()

#creamos un dataframe de los datos de flores
#etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], 
                              columns = iris_dataset.feature_names)

iris_dataframe['target'] = iris_dataset['target']
iris_dataframe['target'].replace({0:'setosa', 1:'versicolor', 2:'virginica'},
                                 inplace = True)

sns.pairplot(iris_dataframe, hue = 'target',  diag_kind="hist")


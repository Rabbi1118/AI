# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:57:34 2021

@author: Rabbi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:55:47 2021

@author: Rabbi
"""

import pandas as pd  #Read Data from CSV file
#from sklearn.preprocessing import LabelEncoder    #Preprocess the data
from sklearn.model_selection import train_test_split    #Split the Data Set: Training Set(<=70%), Test Set(>=30%)
from sklearn.naive_bayes import GaussianNB          #Train The Model using Training Set and a Machine Learning   Algorithm (Ex: Naïve Bayes)
from sklearn import metrics


#Import Data
data = pd.read_csv('iris.csv')
print(data)

'''
#Preprocess Data
number = LabelEncoder()
data['sepal_length'] = number.fit_transform(data['sepal_length'])
data['sepal_width'] = number.fit_transform(data['sepal_width'])
data['petal_length'] = number.fit_transform(data['petal_length'])
data['petal_width'] = number.fit_transform(data['petal_width'])
data['Class'] = number.fit_transform(data['Class'])

print("\n\nAfter Preprocessing: ")
print(data)
'''

#Split Data
feature = ['sepal_length','sepal_width','petal_length','petal_width'] 
target = 'Class'
X_train,X_test,Y_train,Y_test = train_test_split(data[feature], data[target], test_size=0.3, random_state=1)


#Train the model
model = GaussianNB()
model.fit(X_train, Y_train)


#Test the model
Y_pred = model.predict(X_test)
print("Y_test")
print(Y_test)
print("Y_Pred")
print(Y_pred)
print("\nAccuracy: ", metrics.accuracy_score(Y_test, Y_pred))

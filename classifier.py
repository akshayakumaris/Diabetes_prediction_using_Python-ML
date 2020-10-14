# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:40:43 2020

@author: user
"""

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


df=pd.read_csv('diabetes.csv')

x=df.iloc[:,0:8].values
y=df.iloc[:,-1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)



RFC=RandomForestClassifier()
RFC.fit(x_train,y_train)

y_pred=RFC.predict(x_test)
print(accuracy_score(y_test,y_pred))

pickle_out=open('RFC.pkl','wb')
pickle.dump(RFC,pickle_out)
pickle_out.close()
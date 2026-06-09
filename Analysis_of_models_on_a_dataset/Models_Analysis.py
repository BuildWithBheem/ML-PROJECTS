import pandas as pd
import numpy as np

df= pd.read_csv('/content/diabetes.csv')

df.corr(numeric_only = True)

df.isnull().sum()

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()

log_reg.fit(x_train,y_train)

x_pred1 = log_reg.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,x_pred1)

from sklearn.svm import SVC
svc_model = SVC(kernel = 'linear')

svc_model.fit(x_train,y_train)

x_pred2 = svc_model.predict(x_test)
accuracy_score(y_test,x_pred2)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators = 200, criterion = 'entropy')
rfc.fit(x_train,y_train)
x_pred3 = rfc.predict(x_test)

accuracy_score(y_test,x_pred3)

from sklearn.metrics import confusion_matrix,precision_score
print('Logistic Reg :')
confusion_matrix(y_test,x_pred1)

precision_score(y_test,x_pred1)

print('SVC :')
confusion_matrix(y_test,x_pred2)

precision_score(y_test,x_pred2)

print('Random Forest :')
confusion_matrix(y_test,x_pred3)

precision_score(y_test,x_pred3)

import joblib as jb
jb.dump(svc_model,'svc_model')
jb.dump(log_reg,'Logistic_reg_model')
jb.dump(rfc,'Random_forest_classifier')
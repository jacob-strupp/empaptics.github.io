
import pandas as pd
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

#-import and partition 
df = pd.read_csv("EEG_IADS.csv", header = 0)
x = df.iloc[:, 1:-2]  
y = df.iloc[: , -1]  
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=109) 

#-train ovo classifier 
params_grid =  {'C': [0.1,1, 10, 100], 'gamma': [1,0.1,0.01,0.001],'kernel': ['rbf', 'poly', 'sigmoid']}
clf = GridSearchCV(svm.SVC(),params_grid)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Classification Report:",classification_report(y_test, y_pred))
print("Cross-validation:",cross_val_score(clf, x, y, cv=10))


# one-class svm for imbalanced binary classification
from sklearn.metrics import precision_recall_fscore_support, classification_report,confusion_matrix, precision_recall_curve
import pandas as pd
import pickle

test = pd.read_csv('./Test.csv')

testX = test.drop(['label','Pattern'], axis = 1) 
print(testX.shape)
testy = test.label

filename = 'oc-svm.sav'
 
loaded_iforest = pickle.load(open(filename, 'rb'))
yhat = loaded_iforest.predict(testX)
testy[testy == 1] = -1
testy[testy == 0] = 1

print(classification_report(testy, yhat))

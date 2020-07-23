# isolation forest for imbalanced classification
import pickle
from sklearn.metrics import precision_recall_fscore_support, classification_report,confusion_matrix, precision_recall_curve
import pandas as pd

test = pd.read_csv('./Test.csv')

testX = test.drop(['label','Pattern'], axis = 1) 
testy = test.label

filename = 'iforest_model.sav'
loaded_iforest = pickle.load(open(filename, 'rb'))
yhat = loaded_iforest.predict(testX)
testy[testy == 1] = -1
testy[testy == 0] = 1
print(classification_report(testy, yhat))

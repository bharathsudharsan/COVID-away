from sklearn.metrics import precision_recall_fscore_support, classification_report,confusion_matrix, precision_recall_curve
import numpy as np
import pandas as pd
import tensorflow as tf

model = tf.keras.models.load_model('CNN_Acc+Gyro.h5')

acc_gyro_test = pd.read_csv("Test.csv")

acc_gyro_X1 = acc_gyro_test.drop(['Pattern','Mbar_mean','Mbar_std','Mbar_mad','Mbar_iqr','Mbar_skew',
                'Mbar_entropy','Mbar_arCoeff_1','Mbar_arCoeff_2','Mbar_arCoeff_3','Mbar_arCoeff_4','Mbar_kurtosis',
                'Mbar_energy','CosO_mean','CosO_std','CosO_mad','CosO_iqr','CosO_skew','CosO_entropy',
                'CosO_arCoeff_1','CosO_arCoeff_2','CosO_arCoeff_3','CosO_arCoeff_4','CosO_kurtosis','CosO_energy', 'label'], axis=1)

acc_gyro_y1 = acc_gyro_test.label

yhat = model.predict(acc_gyro_X1)
yhat = pd.DataFrame(yhat)
yhat = yhat[0].tolist()

def all_30_or_up(yhat):
    for i,item in enumerate(yhat):
        if item > 0.80:
            yhat[i] = 1
        else:
            yhat[i] = -1
    return yhat

y_1 = pd.DataFrame(acc_gyro_y1)
y_1 = y_1['label'].tolist()

all_30_or_up(yhat)

print(classification_report(y_1, yhat))

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

open("acc_gyro_model_auto_tflite.tflite", "wb").write(tflite_model)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_model = converter.convert()

open("acc_gyro_model_auto_tflite_quantized.tflite", "wb").write(tflite_model)


autoencoder_model_quantized = tf.lite.Interpreter('acc_gyro_model_auto_tflite_quantized.tflite')
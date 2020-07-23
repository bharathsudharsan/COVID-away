from sklearn.metrics import precision_recall_fscore_support, classification_report,confusion_matrix, precision_recall_curve
import numpy as np
import pandas as pd
import tensorflow as tf

model = tf.keras.models.load_model('CNN_Acc.h5')

acc_test = pd.read_csv("Test.csv")

acc_X1 = acc_test.drop(['Pattern','GYR_x_axis_mean','GYR_y_axis_mean','GYR_z_axis_mean',
                      'GYR_x_axis_std','GYR_y_axis_std','GYR_z_axis_std','GYR_x_axis_mad',
                      'GYR_y_axis_mad','GYR_z_axis_mad','GYR_xy_axis_corr','GYR_xz_axis_corr',
                      'GYR_yz_axis_corr','GYR_x_axis_iqr','GYR_y_axis_iqr','GYR_z_axis_iqr',
                      'GYR_x_axis_skew','GYR_y_axis_skew','GYR_z_axis_skew',
                      'GYR_x_axis_entropy','GYR_y_axis_entropy','GYR_z_axis_entropy',
                      'GYR_x_axis_arCoeff_1','GYR_x_axis_arCoeff_2','GYR_x_axis_arCoeff_3',
                      'GYR_x_axis_arCoeff_4','GYR_y_axis_arCoeff_1','GYR_y_axis_arCoeff_2',
                      'GYR_y_axis_arCoeff_3','GYR_y_axis_arCoeff_4','GYR_z_axis_arCoeff_1',
                      'GYR_z_axis_arCoeff_2','GYR_z_axis_arCoeff_3','GYR_z_axis_arCoeff_4',
                      'GYR_x_axis_kurtosis','GYR_y_axis_kurtosis','GYR_z_axis_kurtosis',
                      'GYR_x_axis_energy','GYR_y_axis_energy','GYR_z_axis_energy',
                      'Mbar_mean','Mbar_std','Mbar_mad','Mbar_iqr','Mbar_skew',
                      'Mbar_entropy','Mbar_arCoeff_1','Mbar_arCoeff_2',
                      'Mbar_arCoeff_3','Mbar_arCoeff_4','Mbar_kurtosis','Mbar_energy','CosO_mean',
                      'CosO_std','CosO_mad','CosO_iqr','CosO_skew','CosO_entropy','CosO_arCoeff_1',
                      'CosO_arCoeff_2','CosO_arCoeff_3','CosO_arCoeff_4','CosO_kurtosis','CosO_energy','label'], axis=1)

acc_y1 = acc_test.label

yhat = model.predict(acc_X1)

yhat = pd.DataFrame(yhat)

yhat = yhat[0].tolist()

def all_30_or_up(yhat):
    for i,item in enumerate(yhat):
        if item > 0.80:
            yhat[i] = 1
        else:
            yhat[i] = -1
    return yhat

y_1 = pd.DataFrame(acc_y1)
y_1 = y_1['label'].tolist()

all_30_or_up(yhat)
print(classification_report(y_1, yhat))

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("acc_model_auto_tflite.tflite", "wb").write(tflite_model)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_model = converter.convert()

open("acc_model_auto_tflite_quantized.tflite", "wb").write(tflite_model)


autoencoder_model_quantized = tf.lite.Interpreter('acc_model_auto_tflite_quantized.tflite')
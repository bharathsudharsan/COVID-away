# COVID-away CNNs

To replicate the results from the below Table, one by one run: 
 - 'python [COVID-away_CNN_Acc.py](https://github.com/bharathsudharsan/COVID-away/blob/master/COVID-away%20CNNs/COVID-away_CNN_Acc.py)'
 - 'python [COVID-away_CNN_Acc+Gyro.py](https://github.com/bharathsudharsan/COVID-away/blob/master/COVID-away%20CNNs/COVID-away_CNN_Acc%2BGyro.py)'
 
 The [Test.csv](https://github.com/bharathsudharsan/COVID-away/blob/master/COVID-away%20CNNs/Test.csv) contains 100 new motion patterns for both hand-to-face \& non-hand-to-face motion data recorded using a new, fourth volunteer.

![alt text](https://github.com/bharathsudharsan/COVID-away/blob/master/Table3_result.PNG)

The COVID-away CNNs, once deployed on smartwatches, can instantly warn the users when their hands are moved (un-intentionally) to the face.

 - The first model, "COVID-away_CNN_Acc.h5" requires only Accelerometer data (Acc = 39 features) to detect hand-to-face movement. 
 - The second model, "COVID-away_CNN_Acc+Gyro.h5" was trained using additional Gyroscope data (Acc+Gyro = 78 features), hence requiring real-time data from two sensors for hand-to-face movement detection. 

In order to produce a smartwatch friendly version of the above models, we optimize the CNNs by quantizing both its weights & activations to INT-8. The latency & size optimized versions of above models are:

- COVID-away_CNN_Acc_tflite_quantized.tflite
- COVID-away_CNN_Acc+Gyro_tflite_quantized.tflite

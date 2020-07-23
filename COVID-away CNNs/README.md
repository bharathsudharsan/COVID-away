## COVID-away CNNs
To replicate the results from Table 3, one by one run: "python COVID-away_CNN_Acc.py", then "COVID-away_CNN_Acc+Gyro.py". The Test.csv contains 100 new motion patterns for both hand-to-face \& non-hand-to-face motion data recorded using a new, fourth volunteer.
Our COVID-away CNNs, once deployed on smartwatches, can instantly warn the users when their hands are moved (un-intentionally) to the face.
1. The first model, "COVID-away_CNN_Acc.h5" requires only Accelerometer data (Acc = 39 features) to detect hand-to-face movement. 
2. The second model, "COVID-away_CNN_Acc+Gyro.h5" was trained using additional Gyroscope data (Acc+Gyro = 78 features), hence requiring real-time data from two sensors for hand-to-face movement detection. 

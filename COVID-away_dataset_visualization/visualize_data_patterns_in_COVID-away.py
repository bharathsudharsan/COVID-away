
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams.update({'xtick.bottom' : False, 'axes.titlepad':5})

from scipy import signal
import matplotlib.pyplot as plt

fig, axes = plt.subplots(4,1, figsize=(4, 10), sharex=True, dpi=120)

b, a = signal.butter(3, 0.05)

pattern = input("Enter the pattern number (0-2071) of hand-to-face motion data you want to visualize from the COVID-away dataset: ") 
Acc_file ='./COVID-away_dataset/Pattern_'+ pattern + '/Accelerometer.csv'
Gyro_file = './COVID-away_dataset/Pattern_'+ pattern + '/Gyroscope.csv'
Pressure_file = './COVID-away_dataset/Pattern_'+ pattern + '/Pressure.csv'
RVect_file ='./COVID-away_dataset/Pattern_'+ pattern + '/RotationVector.csv'

df_orig = pd.read_csv(Acc_file, index_col= 1)
df_orig2 = pd.read_csv(Gyro_file, index_col= 1)
df_orig3 = pd.read_csv(Pressure_file, index_col= 1)
df_orig4 = pd.read_csv(RVect_file, index_col= 1)



x = signal.filtfilt(b, a, df_orig['X'])
y = signal.filtfilt(b, a, df_orig['Y'])
z = signal.filtfilt(b, a, df_orig['Z'])

x = pd.DataFrame(x)
y = pd.DataFrame(y)
z = pd.DataFrame(z)

x.plot(ax=axes[0], color = 'C0', legend = None)
y.plot(ax=axes[0], color = 'C1', legend = None)
z.plot(ax=axes[0], color = 'C2', legend = None, title='Accelerometer.csv')


x = signal.filtfilt(b, a, df_orig2['X'])
y = signal.filtfilt(b, a, df_orig2['Y'])
z = signal.filtfilt(b, a, df_orig2['Z'])

x = pd.DataFrame(x)
y = pd.DataFrame(y)
z = pd.DataFrame(z)

x.plot(ax=axes[1], color = 'C7', legend = None)
y.plot(ax=axes[1], color = 'C8', legend = None)
z.plot(ax=axes[1], title='Gyroscope.csv', color = 'C9', legend = None)

x = pd.DataFrame(x)
y = pd.DataFrame(y)
z = pd.DataFrame(z)

x = signal.filtfilt(b, a, df_orig3['Millibars'])
x = pd.DataFrame(x)
x.plot(ax=axes[2], title='Pressure.csv', color = 'C6', legend = None)


x = signal.filtfilt(b, a, df_orig4['X'])
y = signal.filtfilt(b, a, df_orig4['Y'])
z = signal.filtfilt(b, a, df_orig4['Z'])
c = signal.filtfilt(b, a, df_orig4['cos'])



x = pd.DataFrame(x)
y = pd.DataFrame(y)
z = pd.DataFrame(z)
c = pd.DataFrame(c)

x.plot(ax=axes[3], color = 'C7', legend = None)
y.plot(ax=axes[3], color = 'C8', legend = None)
z.plot(ax=axes[3], color = 'C9', legend = None)   
c.plot(ax=axes[3], title='RotationVector.csv', color = 'C3', legend = None)

plt.show()
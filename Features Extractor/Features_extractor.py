import os
import time
import pandas as pd
from scipy import stats
import csv
from scipy.stats import skew 
from scipy.stats import entropy
from scipy.stats import iqr
from scipy import spatial
from scipy.stats import norm, kurtosis
import statistics
import numpy as np
import spectrum 
import functools 
#import numpy as np
field0 = ['X']
field1 = ['Y']
field2 = ['Z']
field3 = ['Millibars']
field4 = ['cos']
folder_name = ''
file = open('features_for_patterns_0_to_2071.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Pattern', 'ACC_x_axis_mean', 'ACC_y_axis_mean', 'ACC_z_axis_mean', 'ACC_x_axis_std','ACC_y_axis_std','ACC_z_axis_std', 'ACC_x_axis_mad', 'ACC_y_axis_mad', 'ACC_z_axis_mad', 'ACC_xy_axis_corr', 'ACC_xz_axis_corr','ACC_yz_axis_corr', 'ACC_x_axis_iqr', 'ACC_y_axis_iqr', 'ACC_z_axis_iqr', 'ACC_x_axis_skew', 'ACC_y_axis_skew', 'ACC_z_axis_skew','ACC_x_axis_entropy','ACC_y_axis_entropy','ACC_z_axis_entropy', 'ACC_x_axis_arCoeff_1', 'ACC_x_axis_arCoeff_2', 'ACC_x_axis_arCoeff_3', 'ACC_x_axis_arCoeff_4', 'ACC_y_axis_arCoeff_1', 'ACC_y_axis_arCoeff_2', 'ACC_y_axis_arCoeff_3', 'ACC_y_axis_arCoeff_4', 'ACC_z_axis_arCoeff_1', 'ACC_z_axis_arCoeff_2', 'ACC_z_axis_arCoeff_3', 'ACC_z_axis_arCoeff_4','ACC_x_axis_kurtosis','ACC_y_axis_kurtosis','ACC_z_axis_kurtosis', 'ACC_x_axis_energy', 'ACC_y_axis_energy', 'ACC_z_axis_energy',
                 'GYR_x_axis_mean', 'GYR_y_axis_mean', 'GYR_z_axis_mean', 'GYR_x_axis_std','GYR_y_axis_std','GYR_z_axis_std', 'GYR_x_axis_mad', 'GYR_y_axis_mad', 'GYR_z_axis_mad', 'GYR_xy_axis_corr', 'GYR_xz_axis_corr','GYR_yz_axis_corr', 'GYR_x_axis_iqr', 'GYR_y_axis_iqr', 'GYR_z_axis_iqr', 'GYR_x_axis_skew', 'GYR_y_axis_skew', 'GYR_z_axis_skew','GYR_x_axis_entropy','GYR_y_axis_entropy','GYR_z_axis_entropy', 'GYR_x_axis_arCoeff_1', 'GYR_x_axis_arCoeff_2', 'GYR_x_axis_arCoeff_3', 'GYR_x_axis_arCoeff_4', 'GYR_y_axis_arCoeff_1', 'GYR_y_axis_arCoeff_2', 'GYR_y_axis_arCoeff_3', 'GYR_y_axis_arCoeff_4', 'GYR_z_axis_arCoeff_1', 'GYR_z_axis_arCoeff_2', 'GYR_z_axis_arCoeff_3', 'GYR_z_axis_arCoeff_4','GYR_x_axis_kurtosis','GYR_y_axis_kurtosis','GYR_z_axis_kurtosis', 'GYR_x_axis_energy', 'GYR_y_axis_energy', 'GYR_z_axis_energy',
                 'Mbar_mean', 'Mbar_std', 'Mbar_mad', 'Mbar_iqr', 'Mbar_skew','Mbar_entropy', 'Mbar_arCoeff_1', 'Mbar_arCoeff_2', 'Mbar_arCoeff_3', 'Mbar_arCoeff_4','Mbar_kurtosis', 'Mbar_energy',
                 'CosO_mean', 'CosO_std', 'CosO_mad', 'CosO_iqr', 'CosO_skew','CosO_entropy', 'CosO_arCoeff_1', 'CosO_arCoeff_2', 'CosO_arCoeff_3', 'CosO_arCoeff_4','CosO_kurtosis', 'CosO_energy'])
def scan_folder(parent):
    count = 0
    # iterate over all the files in directory 'parent'
    for file_name in os.listdir(parent):

        if file_name.endswith("Gyroscope.csv"):
            file_to_open = folder_name + '/' + file_name
            GYR_x_axis_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field0)
            df = pd.DataFrame(GYR_x_axis_raw) 
            print('i am currently readding Gyroscope file of')
            print(folder_name_in)
            
            GYR_x_axis_raw_mean = df.mean(axis = None, skipna = True)
            GYR_x_axis_raw_mean = list(GYR_x_axis_raw_mean)
            GYR_x_axis_raw_mean = str(GYR_x_axis_raw_mean)[1:-1] 
            print ('GYR_x_axis_raw_mean',GYR_x_axis_raw_mean)
            
            GYR_x_axis_raw_std = df.std(axis = None, skipna = True)
            GYR_x_axis_raw_std = list(GYR_x_axis_raw_std)
            GYR_x_axis_raw_std = str(GYR_x_axis_raw_std)[1:-1] 
            print ('GYR_x_axis_raw_std',GYR_x_axis_raw_std)
            
            GYR_x_axis_raw_mad = stats.median_absolute_deviation(GYR_x_axis_raw)
            GYR_x_axis_raw_mad = list(GYR_x_axis_raw_mad)
            GYR_x_axis_raw_mad = str(GYR_x_axis_raw_mad)[1:-1] 
            print ('GYR_x_axis_raw_mad',GYR_x_axis_raw_mad)
            
            GYR_y_axis_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field1)
            df = pd.DataFrame(GYR_y_axis_raw) 
                        
            GYR_y_axis_raw_mean = df.mean(axis = None, skipna = True)
            GYR_y_axis_raw_mean = list(GYR_y_axis_raw_mean)
            GYR_y_axis_raw_mean = str(GYR_y_axis_raw_mean)[1:-1] 
            print ('GYR_y_axis_raw_mean',GYR_y_axis_raw_mean)
            
            GYR_y_axis_raw_std = df.std(axis = None, skipna = True)
            GYR_y_axis_raw_std = list(GYR_y_axis_raw_std)
            GYR_y_axis_raw_std = str(GYR_y_axis_raw_std)[1:-1] 
            print ('GYR_y_axis_raw_std',GYR_y_axis_raw_std)
            
            GYR_y_axis_raw_mad = stats.median_absolute_deviation(GYR_y_axis_raw)
            GYR_y_axis_raw_mad = list(GYR_y_axis_raw_mad)
            GYR_y_axis_raw_mad = str(GYR_y_axis_raw_mad)[1:-1] 
            print ('GYR_y_axis_raw_mad',GYR_y_axis_raw_mad)
            
            GYR_z_axis_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field2)
            df = pd.DataFrame(GYR_z_axis_raw) 
                        
            GYR_z_axis_raw_mean = df.mean(axis = None, skipna = True)
            GYR_z_axis_raw_mean = list(GYR_z_axis_raw_mean)
            GYR_z_axis_raw_mean = str(GYR_z_axis_raw_mean)[1:-1] 
            print ('GYR_z_axis_raw_mean',GYR_z_axis_raw_mean)
            
            GYR_z_axis_raw_std = df.std(axis = None, skipna = True)
            GYR_z_axis_raw_std = list(GYR_z_axis_raw_std)
            GYR_z_axis_raw_std = str(GYR_z_axis_raw_std)[1:-1] 
            print ('GYR_z_axis_raw_std',GYR_z_axis_raw_std)
            
            GYR_z_axis_raw_mad = stats.median_absolute_deviation(GYR_z_axis_raw)
            GYR_z_axis_raw_mad = list(GYR_z_axis_raw_mad)
            GYR_z_axis_raw_mad = str(GYR_z_axis_raw_mad)[1:-1] 
            print ('GYR_z_axis_raw_mad',GYR_z_axis_raw_mad)
            
            GYR_x_axis_raw = pd.DataFrame(GYR_x_axis_raw)
            GYR_x_axis_raw = GYR_x_axis_raw['X'].tolist()
            GYR_y_axis_raw = pd.DataFrame(GYR_y_axis_raw)
            GYR_y_axis_raw = GYR_y_axis_raw['Y'].tolist()
            GYR_z_axis_raw = pd.DataFrame(GYR_z_axis_raw)
            GYR_z_axis_raw = GYR_z_axis_raw['Z'].tolist()

            GYR_xy_axis_raw_corr, _ = stats.pearsonr(GYR_x_axis_raw, GYR_y_axis_raw)
            print ('GYR_xy_axis_raw_corr',GYR_xy_axis_raw_corr)
            GYR_xz_axis_raw_corr, _ = stats.pearsonr(GYR_x_axis_raw, GYR_z_axis_raw)
            print ('GYR_xz_axis_raw_corr',GYR_xz_axis_raw_corr)
            GYR_yz_axis_raw_corr, _ = stats.pearsonr(GYR_y_axis_raw, GYR_z_axis_raw)
            print ('GYR_yz_axis_raw_corr',GYR_yz_axis_raw_corr)
            
            
            GYR_x_axis_raw_iqr = iqr(GYR_x_axis_raw)
            print('GYR_x_axis_raw_iqr',GYR_x_axis_raw_iqr)
            GYR_y_axis_raw_iqr=iqr(GYR_y_axis_raw)
            print('GYR_y_axis_raw_iqr',GYR_y_axis_raw_iqr)
            GYR_z_axis_raw_iqr= iqr(GYR_z_axis_raw)
            print('GYR_z_axis_raw_iqr',GYR_z_axis_raw_iqr)
            
            GYR_x_axis_raw_skew = skew(GYR_x_axis_raw)
            print('GYR_x_axis_raw_skew',GYR_x_axis_raw_skew)
            GYR_y_axis_raw_skew=skew(GYR_y_axis_raw)
            print('GYR_y_axis_raw_skew',GYR_y_axis_raw_skew)
            GYR_z_axis_raw_skew= skew(GYR_z_axis_raw)
            print('GYR_z_axis_raw_skew',GYR_z_axis_raw_skew)
            
            GYR_x_axis_raw_entropy = entropy(GYR_x_axis_raw)
            print('GYR_x_axis_raw_entropy',GYR_x_axis_raw_entropy)
            GYR_y_axis_raw_entropy=entropy(GYR_y_axis_raw)
            print('GYR_y_axis_raw_entropy',GYR_y_axis_raw_entropy)
            GYR_z_axis_raw_entropy= entropy(GYR_z_axis_raw)
            print('GYR_z_axis_raw_entropy',GYR_z_axis_raw_entropy)
            
            GYR_x_axis_raw_arCoeff, energy_x, reflectioncoeffs_x  = spectrum.arburg(GYR_x_axis_raw, 4)
            GYR_x_axis_raw_arCoeff_1 = str(GYR_x_axis_raw_arCoeff[0])[1:-1]
            GYR_x_axis_raw_arCoeff_2 = str(GYR_x_axis_raw_arCoeff[1])[1:-1]
            GYR_x_axis_raw_arCoeff_3 = str(GYR_x_axis_raw_arCoeff[2])[1:-1]
            GYR_x_axis_raw_arCoeff_4 = str(GYR_x_axis_raw_arCoeff[3])[1:-1]
            print('GYR_x_axis_raw_arCoeff',GYR_x_axis_raw_arCoeff)
            GYR_y_axis_raw_arCoeff, energy_y, reflectioncoeffs_y= spectrum.arburg(GYR_y_axis_raw, 4)
            GYR_y_axis_raw_arCoeff_1 = str(GYR_y_axis_raw_arCoeff[0])[1:-1]
            GYR_y_axis_raw_arCoeff_2 = str(GYR_y_axis_raw_arCoeff[1])[1:-1]
            GYR_y_axis_raw_arCoeff_3 = str(GYR_y_axis_raw_arCoeff[2])[1:-1]
            GYR_y_axis_raw_arCoeff_4 = str(GYR_y_axis_raw_arCoeff[3])[1:-1]
            print('GYR_y_axis_raw_arCoeff',GYR_y_axis_raw_arCoeff)
            GYR_z_axis_raw_arCoeff, energy_z, reflectioncoeffs_z= spectrum.arburg(GYR_z_axis_raw, 4)
            GYR_z_axis_raw_arCoeff_1 = str(GYR_z_axis_raw_arCoeff[0])[1:-1]
            GYR_z_axis_raw_arCoeff_2 = str(GYR_z_axis_raw_arCoeff[1])[1:-1]
            GYR_z_axis_raw_arCoeff_3 = str(GYR_z_axis_raw_arCoeff[2])[1:-1]
            GYR_z_axis_raw_arCoeff_4 = str(GYR_z_axis_raw_arCoeff[3])[1:-1]
            print('GYR_z_axis_raw_arCoeff',GYR_z_axis_raw_arCoeff)         
            
            GYR_x_axis_raw_kurtosis = kurtosis(GYR_x_axis_raw)
            print('GYR_x_axis_raw_kurtosis',GYR_x_axis_raw_kurtosis)
            GYR_y_axis_raw_kurtosis=kurtosis(GYR_y_axis_raw)
            print('GYR_y_axis_raw_kurtosis',GYR_y_axis_raw_kurtosis)
            GYR_z_axis_raw_kurtosis= kurtosis(GYR_z_axis_raw)
            print('GYR_z_axis_raw_kurtosis',GYR_z_axis_raw_kurtosis)
            GYR_x_axis_raw_energy = (functools.reduce(lambda x,y: x+y*y,GYR_x_axis_raw))/len(GYR_x_axis_raw) 
            print('GYR_x_axis_raw_energy',GYR_x_axis_raw_energy)
            GYR_y_axis_raw_energy= (functools.reduce(lambda x,y: x+y*y,GYR_y_axis_raw))/len(GYR_y_axis_raw)
            print('GYR_y_axis_raw_energy',GYR_y_axis_raw_energy)
            GYR_z_axis_raw_energy= (functools.reduce(lambda x,y: x+y*y,GYR_z_axis_raw))/len(GYR_z_axis_raw)
            print('GYR_z_axis_raw_energy',GYR_z_axis_raw_energy)
            count = count + 1


        elif file_name.endswith("Pressure.csv"):
            file_to_open = folder_name + '/' + file_name
            Mbar_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field3)
            df = pd.DataFrame(Mbar_raw) 
            print('i am currently readding Pressure file of')
            print(folder_name_in)
            
            Mbar_raw_mean = df.mean(axis = None, skipna = True)
            Mbar_raw_mean = list(Mbar_raw_mean)
            Mbar_raw_mean = str(Mbar_raw_mean)[1:-1] 
            print ('Mbar_raw_mean',Mbar_raw_mean)
            
            Mbar_raw_std = df.std(axis = None, skipna = True)
            Mbar_raw_std = list(Mbar_raw_std)
            Mbar_raw_std = str(Mbar_raw_std)[1:-1] 
            print ('Mbar_raw_std',Mbar_raw_std)
            
            Mbar_raw_mad = stats.median_absolute_deviation(Mbar_raw)
            Mbar_raw_mad = list(Mbar_raw_mad)
            Mbar_raw_mad = str(Mbar_raw_mad)[1:-1] 
            print ('Mbar_raw_mad',Mbar_raw_mad)
            
            Mbar_raw = pd.DataFrame(Mbar_raw)
            Mbar_raw = Mbar_raw['Millibars'].tolist()
            
            Mbar_raw_iqr = iqr(Mbar_raw)
            print('Mbar_raw_iqr',Mbar_raw_iqr)
            
            Mbar_raw_skew = skew(Mbar_raw)
            
            print('Mbar_raw_skew',Mbar_raw_skew)
            
            Mbar_raw_entropy = entropy(Mbar_raw)
            print('Mbar_raw_entropy',Mbar_raw_entropy)
            
            Mbar_raw_arCoeff, energy_x, reflectioncoeffs_x  = spectrum.arburg(Mbar_raw, 4)
            Mbar_raw_arCoeff_1 = str(Mbar_raw_arCoeff[0])[1:-1]
            Mbar_raw_arCoeff_2 = str(Mbar_raw_arCoeff[1])[1:-1]
            Mbar_raw_arCoeff_3 = str(Mbar_raw_arCoeff[2])[1:-1]
            Mbar_raw_arCoeff_4 = str(Mbar_raw_arCoeff[3])[1:-1]
            print('Mbar_raw_arCoeff',Mbar_raw_arCoeff)
            
            Mbar_raw_kurtosis = kurtosis(Mbar_raw)
            print('Mbar_raw_kurtosis',Mbar_raw_kurtosis)
            Mbar_raw_energy = (functools.reduce(lambda x,y: x+y*y,Mbar_raw))/len(Mbar_raw) 
            print('Mbar_raw_energy',Mbar_raw_energy)
            count = count + 1
        elif file_name.endswith("RotationVector.csv"):
            file_to_open = folder_name + '/' + file_name
            CosO = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field4)
            df = pd.DataFrame(CosO) 
            print('i am currently readding RotationVector file of')
            print(folder_name_in)
            
            CosO_mean = df.mean(axis = None, skipna = True)
            CosO_mean = list(CosO_mean)
            CosO_mean = str(CosO_mean)[1:-1] 
            print ('CosO_mean',CosO_mean)
            
            CosO_std = df.std(axis = None, skipna = True)
            CosO_std = list(CosO_std)
            CosO_std = str(CosO_std)[1:-1] 
            print ('CosO_std',CosO_std)
            
            CosO_mad = stats.median_absolute_deviation(CosO)
            CosO_mad = list(CosO_mad)
            CosO_mad = str(CosO_mad)[1:-1] 
            print ('CosO_mad',CosO_mad)
            
            CosO = pd.DataFrame(CosO)
            CosO = CosO['cos'].tolist()
            
            CosO_iqr = iqr(CosO)
            print('CosO_iqr',CosO_iqr)
            
            CosO_skew = skew(CosO)
            
            print('CosO_skew',CosO_skew)
            
            CosO_entropy = entropy(CosO)
            print('CosO_entropy',CosO_entropy)
            
            CosO_arCoeff, energy_x, reflectioncoeffs_x  = spectrum.arburg(CosO, 4)
            CosO_arCoeff_1 = str(CosO_arCoeff[0])[1:-1]
            CosO_arCoeff_2 = str(CosO_arCoeff[1])[1:-1]
            CosO_arCoeff_3 = str(CosO_arCoeff[2])[1:-1]
            CosO_arCoeff_4 = str(CosO_arCoeff[3])[1:-1]
            print('CosO_arCoeff',CosO_arCoeff)
            
            CosO_kurtosis = kurtosis(CosO)
            print('CosO_kurtosis',CosO_kurtosis)
            CosO_energy = (functools.reduce(lambda x,y: x+y*y,CosO))/len(CosO) 
            print('CosO_energy',CosO_energy)
            count = count + 1
        elif file_name.endswith("Accelerometer.csv"):
            file_to_open = folder_name + '/' + file_name
            ACC_x_axis_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field0)
            df = pd.DataFrame(ACC_x_axis_raw) 
            print('i am currently readding Acclerometer file of')
            print(folder_name_in)
            
            ACC_x_axis_raw_mean = df.mean(axis = None, skipna = True)
            ACC_x_axis_raw_mean = list(ACC_x_axis_raw_mean)
            ACC_x_axis_raw_mean = str(ACC_x_axis_raw_mean)[1:-1] 
            print ('ACC_x_axis_raw_mean',ACC_x_axis_raw_mean)
            
            ACC_x_axis_raw_std = df.std(axis = None, skipna = True)
            ACC_x_axis_raw_std = list(ACC_x_axis_raw_std)
            ACC_x_axis_raw_std = str(ACC_x_axis_raw_std)[1:-1] 
            print ('ACC_x_axis_raw_std',ACC_x_axis_raw_std)
            
            ACC_x_axis_raw_mad = stats.median_absolute_deviation(ACC_x_axis_raw)
            ACC_x_axis_raw_mad = list(ACC_x_axis_raw_mad)
            ACC_x_axis_raw_mad = str(ACC_x_axis_raw_mad)[1:-1] 
            print ('ACC_x_axis_raw_mad',ACC_x_axis_raw_mad)
            
            ACC_y_axis_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field1)
            df = pd.DataFrame(ACC_y_axis_raw) 
                        
            ACC_y_axis_raw_mean = df.mean(axis = None, skipna = True)
            ACC_y_axis_raw_mean = list(ACC_y_axis_raw_mean)
            ACC_y_axis_raw_mean = str(ACC_y_axis_raw_mean)[1:-1] 
            print ('ACC_y_axis_raw_mean',ACC_y_axis_raw_mean)
            
            ACC_y_axis_raw_std = df.std(axis = None, skipna = True)
            ACC_y_axis_raw_std = list(ACC_y_axis_raw_std)
            ACC_y_axis_raw_std = str(ACC_y_axis_raw_std)[1:-1] 
            print ('ACC_y_axis_raw_std',ACC_y_axis_raw_std)
            
            ACC_y_axis_raw_mad = stats.median_absolute_deviation(ACC_y_axis_raw)
            ACC_y_axis_raw_mad = list(ACC_y_axis_raw_mad)
            ACC_y_axis_raw_mad = str(ACC_y_axis_raw_mad)[1:-1] 
            print ('ACC_y_axis_raw_mad',ACC_y_axis_raw_mad)
            
            ACC_z_axis_raw = pd.read_csv(file_to_open, skipinitialspace=True, usecols= field2)
            df = pd.DataFrame(ACC_z_axis_raw) 
                        
            ACC_z_axis_raw_mean = df.mean(axis = None, skipna = True)
            ACC_z_axis_raw_mean = list(ACC_z_axis_raw_mean)
            ACC_z_axis_raw_mean = str(ACC_z_axis_raw_mean)[1:-1] 
            print ('ACC_z_axis_raw_mean',ACC_z_axis_raw_mean)
            
            ACC_z_axis_raw_std = df.std(axis = None, skipna = True)
            ACC_z_axis_raw_std = list(ACC_z_axis_raw_std)
            ACC_z_axis_raw_std = str(ACC_z_axis_raw_std)[1:-1] 
            print ('ACC_z_axis_raw_std',ACC_z_axis_raw_std)
            
            ACC_z_axis_raw_mad = stats.median_absolute_deviation(ACC_z_axis_raw)
            ACC_z_axis_raw_mad = list(ACC_z_axis_raw_mad)
            ACC_z_axis_raw_mad = str(ACC_z_axis_raw_mad)[1:-1] 
            print ('ACC_z_axis_raw_mad',ACC_z_axis_raw_mad)
            
            ACC_x_axis_raw = pd.DataFrame(ACC_x_axis_raw)
            ACC_x_axis_raw = ACC_x_axis_raw['X'].tolist()
            ACC_y_axis_raw = pd.DataFrame(ACC_y_axis_raw)
            ACC_y_axis_raw = ACC_y_axis_raw['Y'].tolist()
            ACC_z_axis_raw = pd.DataFrame(ACC_z_axis_raw)
            ACC_z_axis_raw = ACC_z_axis_raw['Z'].tolist()

            ACC_xy_axis_raw_corr, _ = stats.pearsonr(ACC_x_axis_raw, ACC_y_axis_raw)
            print ('ACC_xy_axis_raw_corr',ACC_xy_axis_raw_corr)
            ACC_xz_axis_raw_corr, _ = stats.pearsonr(ACC_x_axis_raw, ACC_z_axis_raw)
            print ('ACC_xz_axis_raw_corr',ACC_xz_axis_raw_corr)
            ACC_yz_axis_raw_corr, _ = stats.pearsonr(ACC_y_axis_raw, ACC_z_axis_raw)
            print ('ACC_yz_axis_raw_corr',ACC_yz_axis_raw_corr)
            
            
            ACC_x_axis_raw_iqr = iqr(ACC_x_axis_raw)
            print('ACC_x_axis_raw_iqr',ACC_x_axis_raw_iqr)
            ACC_y_axis_raw_iqr=iqr(ACC_y_axis_raw)
            print('ACC_y_axis_raw_iqr',ACC_y_axis_raw_iqr)
            ACC_z_axis_raw_iqr= iqr(ACC_z_axis_raw)
            print('ACC_z_axis_raw_iqr',ACC_z_axis_raw_iqr)
            
            ACC_x_axis_raw_skew = skew(ACC_x_axis_raw)
            print('ACC_x_axis_raw_skew',ACC_x_axis_raw_skew)
            ACC_y_axis_raw_skew=skew(ACC_y_axis_raw)
            print('ACC_y_axis_raw_skew',ACC_y_axis_raw_skew)
            ACC_z_axis_raw_skew= skew(ACC_z_axis_raw)
            print('ACC_z_axis_raw_skew',ACC_z_axis_raw_skew)
            
            ACC_x_axis_raw_entropy = entropy(ACC_x_axis_raw)
            print('ACC_x_axis_raw_entropy',ACC_x_axis_raw_entropy)
            ACC_y_axis_raw_entropy=entropy(ACC_y_axis_raw)
            print('ACC_y_axis_raw_entropy',ACC_y_axis_raw_entropy)
            ACC_z_axis_raw_entropy= entropy(ACC_z_axis_raw)
            print('ACC_z_axis_raw_entropy',ACC_z_axis_raw_entropy)
            
            ACC_x_axis_raw_arCoeff, energy_x, reflectioncoeffs_x  = spectrum.arburg(ACC_x_axis_raw, 4)
            ACC_x_axis_raw_arCoeff_1 = str(ACC_x_axis_raw_arCoeff[0])[1:-1]
            ACC_x_axis_raw_arCoeff_2 = str(ACC_x_axis_raw_arCoeff[1])[1:-1]
            ACC_x_axis_raw_arCoeff_3 = str(ACC_x_axis_raw_arCoeff[2])[1:-1]
            ACC_x_axis_raw_arCoeff_4 = str(ACC_x_axis_raw_arCoeff[3])[1:-1]
            print('ACC_x_axis_raw_arCoeff',ACC_x_axis_raw_arCoeff)
            ACC_y_axis_raw_arCoeff, energy_y, reflectioncoeffs_y= spectrum.arburg(ACC_y_axis_raw, 4)
            ACC_y_axis_raw_arCoeff_1 = str(ACC_y_axis_raw_arCoeff[0])[1:-1]
            ACC_y_axis_raw_arCoeff_2 = str(ACC_y_axis_raw_arCoeff[1])[1:-1]
            ACC_y_axis_raw_arCoeff_3 = str(ACC_y_axis_raw_arCoeff[2])[1:-1]
            ACC_y_axis_raw_arCoeff_4 = str(ACC_y_axis_raw_arCoeff[3])[1:-1]
            print('ACC_y_axis_raw_arCoeff',ACC_y_axis_raw_arCoeff)
            ACC_z_axis_raw_arCoeff, energy_z, reflectioncoeffs_z= spectrum.arburg(ACC_z_axis_raw, 4)
            ACC_z_axis_raw_arCoeff_1 = str(ACC_z_axis_raw_arCoeff[0])[1:-1]
            ACC_z_axis_raw_arCoeff_2 = str(ACC_z_axis_raw_arCoeff[1])[1:-1]
            ACC_z_axis_raw_arCoeff_3 = str(ACC_z_axis_raw_arCoeff[2])[1:-1]
            ACC_z_axis_raw_arCoeff_4 = str(ACC_z_axis_raw_arCoeff[3])[1:-1]
            print('ACC_z_axis_raw_arCoeff',ACC_z_axis_raw_arCoeff)         
            
            ACC_x_axis_raw_kurtosis = kurtosis(ACC_x_axis_raw)
            print('ACC_x_axis_raw_kurtosis',ACC_x_axis_raw_kurtosis)
            ACC_y_axis_raw_kurtosis=kurtosis(ACC_y_axis_raw)
            print('ACC_y_axis_raw_kurtosis',ACC_y_axis_raw_kurtosis)
            ACC_z_axis_raw_kurtosis= kurtosis(ACC_z_axis_raw)
            print('ACC_z_axis_raw_kurtosis',ACC_z_axis_raw_kurtosis)
            
            ACC_x_axis_raw_energy = (functools.reduce(lambda x,y: x+y*y,ACC_x_axis_raw))/len(ACC_x_axis_raw) 
            print('ACC_x_axis_raw_energy',ACC_x_axis_raw_energy)
            ACC_y_axis_raw_energy= (functools.reduce(lambda x,y: x+y*y,ACC_y_axis_raw))/len(ACC_y_axis_raw)
            print('ACC_y_axis_raw_energy',ACC_y_axis_raw_energy)
            ACC_z_axis_raw_energy= (functools.reduce(lambda x,y: x+y*y,ACC_z_axis_raw))/len(ACC_z_axis_raw)
            print('ACC_z_axis_raw_energy',ACC_z_axis_raw_energy)
            count = count + 1

            if count == 4:
            
                writer.writerow([folder_name_in, ACC_x_axis_raw_mean, ACC_y_axis_raw_mean, ACC_z_axis_raw_mean, ACC_x_axis_raw_std, ACC_y_axis_raw_std, ACC_z_axis_raw_std, ACC_x_axis_raw_mad, ACC_y_axis_raw_mad, ACC_z_axis_raw_mad,ACC_xy_axis_raw_corr,ACC_xz_axis_raw_corr,ACC_yz_axis_raw_corr, ACC_x_axis_raw_iqr,ACC_y_axis_raw_iqr,ACC_z_axis_raw_iqr,ACC_x_axis_raw_skew,ACC_y_axis_raw_skew,ACC_z_axis_raw_skew,ACC_x_axis_raw_entropy,ACC_y_axis_raw_entropy,ACC_z_axis_raw_entropy, ACC_x_axis_raw_arCoeff_1, ACC_x_axis_raw_arCoeff_2, ACC_x_axis_raw_arCoeff_3, ACC_x_axis_raw_arCoeff_4, ACC_y_axis_raw_arCoeff_1, ACC_y_axis_raw_arCoeff_2, ACC_y_axis_raw_arCoeff_3, ACC_y_axis_raw_arCoeff_4,ACC_z_axis_raw_arCoeff_1, ACC_z_axis_raw_arCoeff_2, ACC_z_axis_raw_arCoeff_3, ACC_z_axis_raw_arCoeff_4, ACC_x_axis_raw_kurtosis,ACC_y_axis_raw_kurtosis,ACC_z_axis_raw_kurtosis,ACC_x_axis_raw_energy,ACC_y_axis_raw_energy,ACC_z_axis_raw_energy, 
                                             GYR_x_axis_raw_mean, GYR_y_axis_raw_mean, GYR_z_axis_raw_mean, GYR_x_axis_raw_std, GYR_y_axis_raw_std, GYR_z_axis_raw_std, GYR_x_axis_raw_mad, GYR_y_axis_raw_mad, GYR_z_axis_raw_mad,GYR_xy_axis_raw_corr,GYR_xz_axis_raw_corr,GYR_yz_axis_raw_corr, GYR_x_axis_raw_iqr,GYR_y_axis_raw_iqr,GYR_z_axis_raw_iqr,GYR_x_axis_raw_skew,GYR_y_axis_raw_skew,GYR_z_axis_raw_skew,GYR_x_axis_raw_entropy,GYR_y_axis_raw_entropy,GYR_z_axis_raw_entropy, GYR_x_axis_raw_arCoeff_1, GYR_x_axis_raw_arCoeff_2, GYR_x_axis_raw_arCoeff_3, GYR_x_axis_raw_arCoeff_4, GYR_y_axis_raw_arCoeff_1, GYR_y_axis_raw_arCoeff_2, GYR_y_axis_raw_arCoeff_3, GYR_y_axis_raw_arCoeff_4,GYR_z_axis_raw_arCoeff_1, GYR_z_axis_raw_arCoeff_2, GYR_z_axis_raw_arCoeff_3, GYR_z_axis_raw_arCoeff_4, GYR_x_axis_raw_kurtosis,GYR_y_axis_raw_kurtosis,GYR_z_axis_raw_kurtosis,GYR_x_axis_raw_energy,GYR_y_axis_raw_energy,GYR_z_axis_raw_energy, 
                                             Mbar_raw_mean, Mbar_raw_std, Mbar_raw_mad, Mbar_raw_iqr, Mbar_raw_skew, Mbar_raw_entropy, Mbar_raw_arCoeff_1, Mbar_raw_arCoeff_2, Mbar_raw_arCoeff_3, Mbar_raw_arCoeff_4, Mbar_raw_kurtosis, Mbar_raw_energy,
                                             CosO_mean, CosO_std, CosO_mad, CosO_iqr, CosO_skew, CosO_entropy, CosO_arCoeff_1, CosO_arCoeff_2, CosO_arCoeff_3, CosO_arCoeff_4, CosO_kurtosis, CosO_energy                                            
                                             ])
                count = 0



        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path):
                # if we're checking a sub-directory, recall this method
                scan_folder(current_path)

for count, filename in enumerate(os.listdir("./COVID-away_dataset/")): 
    folder_name_in ="Pattern_" + str(count)
    folder_name ='./COVID-away_dataset/'+ folder_name_in
    scan_folder(folder_name)

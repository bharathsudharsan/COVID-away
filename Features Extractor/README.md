## Features extractor 

The Features_extractor.py enables users to extract 10 essential features from a single data field in any sensor-based motion dataset. Users can use this code on their datasets, to compute the following features:
1. Mean value                   
1. Standard deviation           
3. Median absolute value        
4. Average sum of the squares   
5. Correlation coefficient      
6. Interquartile range          
7. Frequency signal Skewness    
8. Signal Entropy               
9. Autoregression coefficients  
10. Frequency signal Kurtosis    

We execute this file using "python Features_extractor.py" to compute 102 features for each recorded hand-to-face motion data pattern. Thus computed features are stored in the "Features_for_patterns_0_to_2071.csv" file.
We used, thus extracted features to train COVID-away One-Class Classification Models, and COVID-away CNNs.
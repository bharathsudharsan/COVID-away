# COVID-away: Hand-to-face 3D Motion Dataset and Models for Smartwatches

## Overview

World Health Organisation (WHO) advises that humans must try to avoid touching their eye, nose and mouth,
which is an effective way to stop the spread of viral diseases. This has become even more prominent with
the widespread coronavirus (COVID-19), resulting in a global pandemic. However, we humans on average
touch our face (eye, nose and mouth) 10-20 times an hour, which is often the primary source of getting infected by a variety of viral infections including seasonal Influenza, Coronavirus, Swine
flu, Ebola virus, etc. Touching our face all day long is a quirk of human nature and it is extremely
difficult to train people to avoid touching their face. However, wearable devices and technology can help
to continuously monitor our movements and trigger a timely event reminding people to avoid touching
their face. In this work, we have collected a hand-to-face multi-sensor 3D motion dataset and named it
COVID-away dataset. Using our dataset, we trained models that can continuously monitor human arm/hand
movement using a wearable device and trigger a timely notification (e.g. vibration) to warn the device users
when their hands are moved (unintentionally) towards their face. Our trained COVID-away models can be
easily integrated into an app for smartwatches or fitness bands. Our evaluation shows that the Minimum
Covariance Determinant (MCD) model produces the highest F1-score (0.93) using just the smartwatch’s
accelerometer data (39 features).

**Link to paper:** [http://www.johnbreslin.org/files/publications/20201006_ioth2020.pdf](http://www.johnbreslin.org/files/publications/20201006_ioth2020.pdf)

## Repo contnet 

### COVID-away Dataset

As illustrated in below Figure, we recorded the accelerometer, gyroscope, barometric pressure \& rotation vector data for 2071 dynamic hand-to-face movements, performed with various postures (standing, leaning, slouching, etc.) and wrist orientations (variations in Roll, Pitch, and Yaw).

![alt text](https://github.com/bharathsudharsan/COVID-away/blob/master/Covid-away_dataset_building.png)

### Features Extractor

We provide a generic feature extractor for enabling users to extract 10 essential features (given in below Table 1) from a single data field (dataset row) in any sensor-based motion dataset. Using this, we compute 102 features for each recorded hand-to-face motion data pattern.

![alt text](https://github.com/bharathsudharsan/COVID-away/blob/master/Table1_feature_vectors.PNG)
### COVID-away Models

We provide the beloy type models trained using the features extracted from our COVID-away Dataset. Our models when deployed on smartwatches, instantly warn the users when their hands are moved (un-intentionally) to the face.

1. COVID-away One-Class Classification Models such as One-Class SupportVector Machines (OC-SVM), Isolation Forest (iForest), Minimum Covariance Determinant (MCD),Local Outlier Factor (LOF).
2. COVID-away CNNs and their model size & latency optimized versions.

If the code is useful, please consider citing Covid-away paper using the below BibTex entry:

```
@inproceedings{Bharathcovidaway,
  author    = {Bharath Sudharsan and John G. Breslin and Muhammad Intizar Ali},
  title     = {Avoid Touching Your Face: A Hand-to-face 3D Motion Dataset (COVID-away) and Trained Models for Smartwatches},
  booktitle = {In 10th International Conference on the Internet of Things Companion (IoT ’20 Companion), Malmö, Sweden, October 6–9, 2020},
  publisher = {ACM},
  year      = {2020},
  url       = {https://doi.org/10.1145/3423423.3423433},
  doi       = {10.1145/3423423.3423433},
}
```

For any clarification/further information please don't hesitate to contact me. Email: bharathsudharsan023@gmail.com

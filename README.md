## COVID-away: Hand-to-face 3D Motion Dataset and Models for Smartwatches

### Overview

We humans on average touch our face (eye, nose and mouth) 10-20 times an hour, which is often the primary source of getting infected by a variety of viral infections including seasonal Influenza, Coronavirus, Swine flu, Ebola virus, etc. 

In this work, we have collected a hand-to-face multi-sensor 3D motion dataset and named it COVID-away dataset.

Using our dataset, we trained models that can continuously monitor human arm/hand movement using a wearable device and trigger a timely notification (e.g. vibration) to warn the device users when their hands are moved (unintentionally) towards their face. 

The trained COVID-away models can be easily integrated into an app for smartwatches or fitness bands. 

Evaluation shows that the Minimum Covariance Determinant (MCD) model produces the highest F1-score (0.93) using just the smartwatch’s accelerometer data (39 features).

**Paper:** [https://dl.acm.org/doi/10.1145/3423423.3423433](https://dl.acm.org/doi/10.1145/3423423.3423433)

**Video:** [https://confirm.ie/covid_away/](https://confirm.ie/covid_away/)

**WHO pagge** [https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/en/covidwho-901451](https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/en/covidwho-901451)

### COVID-away Dataset

As shown below, we recorded the accelerometer, gyroscope, barometric pressure \& rotation vector data for 2071 dynamic hand-to-face movements, performed with various postures (standing, leaning, slouching, etc.) and wrist orientations (variations in Roll, Pitch, and Yaw).

![alt text](https://github.com/bharathsudharsan/COVID-away/blob/master/Covid-away_dataset_building.png)

### Features Extractor

We provide a generic feature extractor for enabling users to extract 10 essential features (shown in below Table) from a single data field (dataset row) in any sensor-based motion dataset. Using this, we compute 102 features for each recorded hand-to-face motion data pattern.

![alt text](https://github.com/bharathsudharsan/COVID-away/blob/master/Table1_feature_vectors.PNG)

### COVID-away Models

We provide the beloy type models trained using the features extracted from our COVID-away Dataset. These models when deployed on smartwatches, instantly warn the users when their hands are moved (un-intentionally) to the face.

- COVID-away One-Class Classification Models include:
  -  One-Class SupportVector Machines (OC-SVM)
  -  Isolation Forest (iForest)
  -  Minimum Covariance Determinant (MCD)
  -  Local Outlier Factor (LOF).
- COVID-away CNNs and their model size & latency optimized versions

If the code is useful, please consider citing Covid-away paper using the below BibTex entry:

```
@inproceedings{Bharathcovidaway,
  author    = {Bharath Sudharsan and John G. Breslin and Muhammad Intizar Ali},
  title     = {Avoid Touching Your Face: A Hand-to-face 3D Motion Dataset (COVID-away) and Trained Models for Smartwatches},
  booktitle = {In 10th International Conference on the Internet of Things Companion (IoT ’20 Companion)},
  publisher = {ACM},
  year      = {2020},
  doi       = {10.1145/3423423.3423433},
}
```

For any clarification/further information please don't hesitate to contact me. Email: bharathsudharsan023@gmail.com

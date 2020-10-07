## COVID-away: A Hand-to-face 3D Motion Dataset and Trained Models

This repo contains: 

1. COVID-away dataset: We recorded the accelerometer, gyroscope, barometric pressure \& rotation vector data for 2071 dynamic hand-to-face movements, performed with various postures (standing, leaning, slouching, etc.) and wrist orientations (variations in Roll, Pitch, and Yaw).
2. We provide a generic feature extractor for enabling users to extract 10 essential features from a single data field in any sensor-based motion dataset. Using this, we compute 102 features for each recorded hand-to-face motion data pattern.
3. COVID-away Models: We provide one-class classification models and a CNN trained using the features extracted from our COVID-away Dataset. Our models instantly warn the users when their hands are moved (un-intentionally) to the face.

Please cite this paper if you use the code in this repository as part of your project.

Bharath Sudharsan, Dineshkumar Sundaram, John G. Breslin, and Muhammad Intizar Ali. 2020. Avoid TouchingYour Face: A Hand-to-face 3D Motion Dataset (COVID-away) and Trained Models for Smartwatches. In10thInternational Conference on the Internet of Things Companion (IoT ’20 Companion), October 6–9, 2020, Malmö,Sweden.ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3423423.3423433

For any clarification/further information please don't hesitate to contact me. Email: b.sudharsan1@nuigalway.ie

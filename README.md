## COVID-away: A Hand-to-face 3D Motion Dataset and Trained Models

This repo contains: 

1. COVID-away dataset: We recorded the accelerometer, gyroscope, barometric pressure \& rotation vector data for 2071 dynamic hand-to-face movements, performed with various postures (standing, leaning, slouching, etc.) and wrist orientations (variations in Roll, Pitch, and Yaw).
2. We provide a generic feature extractor for enabling users to extract 10 essential features from a single data field in any sensor-based motion dataset. Using this, we compute 102 features for each recorded hand-to-face motion data pattern.
3. COVID-away Models: We provide one-class classification models and a CNN trained using the features extracted from our COVID-away Dataset. Our models instantly warn the users when their hands are moved (un-intentionally) to the face.

If you use the code in this repository in your work, please cite this paper using the BibTex entry below.

```
@inproceedings{BharathRCENN,
  author    = {Bharath Sudharsan and John G. Breslin and Muhammad Intizar Ali},
  title     = {Avoid Touching Your Face: A Hand-to-face 3D Motion Dataset (COVID-away) and Trained Models for Smartwatches},
  booktitle = {In 10th International Conference on the Internet of Things Companion (IoT ’20 Companion), Malmö, Sweden, October 6–9, 2020 (IoT ’20)},
  publisher = {{ACM}},
  year      = {2020},
  url       = {https://doi.org/10.1145/3423423.3423433},
  doi       = {10.1145/3423423.3423433},
}
```

For any clarification/further information please don't hesitate to contact me. Email: b.sudharsan1@nuigalway.ie

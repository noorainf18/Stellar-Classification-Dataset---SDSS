<p align="center"><img width=100% src="https://github.com/noorainf18/noorainf18/blob/main/Noorain%20Fathima%20-%20Banner.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# STELLAR CLASSIFICATION

Stellar classification involves categorizing stars based on various attributes like temperature, luminosity, and spectral characteristics. The Sloan Digital Sky Survey (SDSS) is a groundbreaking astronomical survey that has provided extensive data on celestial objects, revolutionizing our understanding of the universe.


## Table of Contents

1. Data Description
2. Data Preprocessing
3. Model Used - KNN
4. Model Building
5. Results
6. Deployment
7. License


## Data Description

The data consists of 100,000 observations of space taken by the SDSS (Sloan Digital Sky Survey). Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.
- obj_ID = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS
- alpha = Right Ascension angle (at J2000 epoch)
- delta = Declination angle (at J2000 epoch)
- u = Ultraviolet filter in the photometric system
- g = Green filter in the photometric system
- r = Red filter in the photometric system
- i = Near Infrared filter in the photometric system
- z = Infrared filter in the photometric system
- run_ID = Run Number used to identify the specific scan
- rereun_ID = Rerun Number to specify how the image was processed
- cam_col = Camera column to identify the scanline within the run
- field_ID = Field number to identify each field
- spec_obj_ID = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)
- class = object class (galaxy, star or quasar object)
- redshift = redshift value based on the increase in wavelength
- plate = plate ID, identifies each plate in SDSS
- MJD = Modified Julian Date, used to indicate when a given piece of SDSS data was taken
- fiber_ID = fiber ID that identifies the fiber that pointed the light at the focal plane in each observation


## Data Preprocessing

- Removing irrelevant columns like obj_ID, alpha, delta, run_ID, rerun_ID, cam_col, field_ID, fiber_ID, spec_obj_ID
- Label encoding is used to convert categorical variables into numerical variables.
- To address the class imbalance, we employed the Synthetic Minority Over-sampling Technique (SMOTE).
- Standard Scaler was employed to ensure that all features contribute equally to the model's learning process, preventing biases due to differing scales.
- PCA was implemented to transform high-dimensional data into a lower-dimensional space while retaining most of its variance.


## Model Used - KNN

For classification, KNN was trained on the dataset. KNN is a simple yet effective classification algorithm that assigns labels to data points based on the majority class among their nearest neighbors. It operates by calculating the distance between data points and selecting the most frequent class among the k nearest neighbors.


## Model Building

A pipeline using Scikit-learn's Pipeline class was created to encapsulate a sequence of data processing steps and a machine learning model - Standard Scaler, PCA, and KNN.

PCA works by finding the principal components of the data, which are the directions in the data with the largest variance. The first principal component is the direction with the largest variance, the second principal component is the direction with the second largest variance, and so on. The principal components are orthogonal to each other, meaning that they are uncorrelated and capture independent information about the data. The *n_components* parameter in *PCA(n_components=6)* specifies the number of principal components to keep. In this case, we are keeping 6 principal components. This means that we are reducing the dimensionality of the data from its original number of features to 6 features.

*KNeighborsClassifier* is a type of instance-based learning algorithm that works by finding the k nearest neighbors to a given data point and then classifying the point based on the majority class of those neighbors. The *n_neighbors* parameter in *KNeighborsClassifier(n_neighbors=3, metric='manhattan')* specifies the number of neighbors to consider when classifying a data point. In this case, we are considering 3 neighbors. This means that when classifying a new data point, the algorithm will find the 3 nearest neighbors to that point and then classify the point based on the majority class of those neighbors. The *metric* parameter specifies the distance metric to use when calculating the distance between data points. In this case, we are using the Manhattan distance metric, which is defined as the sum of the absolute differences between the coordinates of two points. Other distance metrics that can be used include Euclidean distance and Minkowski distance.


## Results

The model has high precision, recall, and F1 score for all three classes, indicating that it is performing well. The overall accuracy of the model is 0.97, indicating that it is correctly classifying 97% of the samples. The macro-average and weighted average metrics are also high, indicating that the model is performing well across all classes.


## Deployment

Taking the model from development to deployment, Flask - a powerful web framework for Python - was utilized.


## License

MIT License

Copyright (c) 2024 Noorain Fathima

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

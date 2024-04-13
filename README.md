# KernelPCA

## Description
This project implements the Kernel PCA technique for novelty detection as explored in the paper by Heiko Hoffmann[1]. The technique extends the traditional PCA to handle non-linear data distributions and is particularly good at identifying novel patterns in datasets where novel examples are rare compared to normal examples. This repository contains the code implementation and dataset samples for replicating the study's findings on synthetic and real-world datasets, including handwritten digits and breast-cancer cytology.

## Key Features
* **Kernel PCA Implementation:** Core implementation of the Kernel PCA algorithm.
* **Novelty Detection:** Utilization of Kernel PCA for detecting novel instances effectively in datasets.
* **Datasets Included:** Examples using synthetic distributions and real-world datasets for hands-on experimentation.
* **Performance Evaluation:** Tools and scripts to assess the performance of the novelty detection using ROC analysis.

## How It Works
The implementation maps training data into an infinite-dimensional feature space, where the principal components of the data distribution are extracted. Novelty is measured by the squared distance to the principal subspace in this feature space. This approach has demonstrated competitive performance in the studied applications.

## <a name="ref"> </a> References
[1] Heiko Hoffmann. “Kernel PCA for novelty detection”. In: Pattern Recognition 40.3 (2007), pp. 863–874: https://www.sciencedirect.com/science/article/pii/S0031320306003414

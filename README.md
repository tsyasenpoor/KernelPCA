# KernelPCA

## Description
This project implements the Kernel PCA technique for novelty detection as explored in the paper by [Heiko Hoffmann](#ref) [1]. The technique extends the traditional PCA to handle non-linear data distributions and is particularly good at identifying novel patterns in datasets where novel examples are rare compared to normal examples. This repository contains the code implementation and dataset samples for replicating the study's findings on synthetic and real-world datasets, including handwritten digits and breast-cancer cytology.

## Key Features
* **Kernel PCA Implementation:** Core implementation of the Kernel PCA algorithm.
* **Novelty Detection:** Utilization of Kernel PCA for detecting novel instances effectively in datasets.
* **Datasets Included:** Examples using synthetic distributions and real-world datasets for hands-on experimentation.
* **Performance Evaluation:** Tools and scripts to assess the performance of the novelty detection using ROC analysis.

## How It Works
The implementation maps training data into an infinite-dimensional feature space, where the principal components of the data distribution are extracted. Novelty is measured by the squared distance to the principal subspace in this feature space. This approach has demonstrated competitive performance in the studied applications.

## Results and Analysis
As mentioned in our report, we applied the KPCA method on many synthetic and real world data sets. Here we'll take a look at some of the main results we got and we'll compare the with the results mentioned in the [paper](#ref) [1].

### Testing the Square Data
Our implementation has been meticulously tested against various hyperparameter settings, including the kernel width σ and the number of eigenvectors q. The plots produced (see Figure 1) demonstrate that our results closely mirror those of the original paper, indicating a high degree of accuracy in our code.


#### Key Observations:

**Influence of Kernel Width (σ)**: A larger σ results in a smoother decision boundary. This trend suggests that a broader neighborhood is considered in the high-dimensional feature space mapping with increasing σ values.

**Effect of Eigenvectors (q)**: Altering the number of eigenvectors from 0 to 40 does not significantly change the shape of the decision boundary within this dataset. However, it is an important parameter that can affect the amount of variance captured from the data

Our findings affirm the robustness of our Kernel PCA implementation. The plots reveal that different σ values adjust the flexibility of the model, whereas the selection of q defines the level of detail in the dimensionality-reduced space.

## <a name="ref"> </a> References
[1] Heiko Hoffmann. “Kernel PCA for novelty detection”. In: Pattern Recognition 40.3 (2007), pp. 863–874: https://www.sciencedirect.com/science/article/pii/S0031320306003414

# Customer Churn Analysis using Machine Learning

## Project Overview

This project analyses customer churn in the telecommunications industry using machine learning techniques. The objective is to prepare the customer dataset, identify meaningful customer segments through clustering, and build predictive models to support customer retention strategies.

This repository contains the deliverables for **Stage 2: Data Preparation and Clustering Analysis**.

---

## Repository Structure

```
Customer-churn-Analysis
│
├── Data_Preparation
│   ├── data_preparation.ipynb
│   ├── preprocessed_dataset.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   ├── y_test.csv
│   ├── train_test_split_summary.csv
│   ├── preprocessing_pipeline.joblib
│   └── scaling_techniques_documentation.pdf
│
├── Clustering_Analysis
│   ├── Clustering_code.ipynb
│   ├── Optimal number of Cluster.pdf
│   ├── X_cluster_scaled.csv
│   ├── scaler.pkl
│   │
│   ├── Trained K-Means Model
│   │   ├── kmeans_model.pkl
│   │   ├── train_kmeans.py
│   │   └── README.md
│   │
│   └── Visualization
│       ├── 1_churn_distribution.png
│       ├── PCA_visualization.png
│       ├── Silhouette_analysis.png
│       ├── characteristic_visualization.png
│       ├── churn_rate.csv
│       ├── cluster_summary.csv
│       └── other analysis outputs
│
└── README.md

```

---

# Stage 2 Deliverables

## Data Preparation

The data preparation stage included:

- Data cleaning and preprocessing
- Handling missing values
- Encoding categorical variables
- Splitting the dataset into training and testing datasets
- Feature scaling using StandardScaler
- Saving the preprocessing pipeline

Outputs include:

- Preprocessed dataset
- Training dataset
- Testing dataset
- Train/Test split summary
- Preprocessing pipeline
- Documentation of scaling techniques

---

## Clustering Analysis

Customer segmentation was performed using the K-Means clustering algorithm.

The clustering workflow included:

- Feature scaling
- Elbow Method
- Silhouette Analysis
- Selection of the optimal number of clusters
- Training the final K-Means model
- Cluster visualisation using PCA
- Customer segment interpretation

Outputs include:

- Trained K-Means model
- Scaled clustering dataset
- Cluster visualisations
- Cluster summary
- Churn analysis by cluster

---

# Technologies Used

- Python 3
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

# Machine Learning Techniques

## Data Preparation

- Missing value handling
- Label Encoding
- Train/Test Split
- StandardScaler

## Clustering

- K-Means Clustering
- Elbow Method
- Silhouette Score
- PCA for visualisation

---

# Business Objective

The purpose of this project is to identify customer groups with similar behaviour and support business decisions aimed at reducing customer churn.

The generated customer segments can be used to:

- Improve customer retention
- Design targeted marketing campaigns
- Identify high-risk customers
- Support future predictive modelling

---

# Authors

Project Team

- **Tanveer Abbas** – Project Manager & Data Analyst (Predictive Modelling)
- **Sarmad** – Data Engineer
- **Tashi** – Data Analyst (Clustering Analysis)
- **Gaurav** – Business Analyst

---

# Future Work

Stage 3 will extend this project by developing an Artificial Neural Network (ANN) model to predict customer churn and evaluate model performance using standard classification metrics.

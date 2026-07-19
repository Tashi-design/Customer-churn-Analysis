# Customer Churn Prediction – Stage 2: Data Preparation and Clustering Analysis

## Project Overview

This repository contains the Stage 2 deliverables for the Customer Churn Prediction project. The objective of this stage is to prepare the telecom customer dataset for machine learning and perform customer segmentation using K-Means clustering.

The project focuses on data preprocessing, feature engineering, train-test splitting, feature scaling, and clustering analysis to identify meaningful customer groups that can support business decision-making and improve customer retention strategies.

---

## Team Members

| Name | Role |
|------|------|
| Tanveer Abbas | Project Manager & Data Analyst (Predictive Modelling) |
| Sarmad | Data Engineer |
| Tashi | Data Analyst (Clustering Analysis) |
| Gaurav | Business Analyst |

---

## Project Objectives

- Prepare and clean the telecom customer dataset.
- Handle missing values and encode categorical variables.
- Split the dataset into training and testing datasets.
- Apply feature scaling using StandardScaler.
- Identify the optimal number of customer clusters.
- Train a K-Means clustering model.
- Visualise and interpret customer segments.
- Generate business insights to support customer retention strategies.

---

## Repository Structure

```
Stage 2/

├── content/
│   └── data/
│       └── Dataset_ATS_v2.csv

├── outputs/
│   ├── cleaned_dataset.csv
│   ├── encoded_dataset.csv
│   ├── scaled_dataset.csv
│   ├── clustered_dataset.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   ├── y_test.csv
│   ├── X_train_scaled.csv
│   ├── X_test_scaled.csv
│   ├── KMeans_Model.pkl
│   └── Visualisation Images (.png)

├── script.ipynb

├── Scaling_Clustering_and_Datasets_Documentation.txt

└── README.md
```

---

## Data Preparation

The following preprocessing steps were completed:

- Data quality inspection
- Missing value handling
- Duplicate removal
- Encoding of categorical variables
- Feature selection
- Train-test split (80% training, 20% testing)
- Feature scaling using StandardScaler


---

## Clustering Analysis

Customer segmentation was performed using the K-Means clustering algorithm.

The workflow includes:

- Elbow Method
- Silhouette Score evaluation
- Selection of the optimal number of clusters
- Training the K-Means model
- PCA-based cluster visualisation
- Cluster profiling and business interpretation

The trained K-Means model has been saved for future use.

---

## Outputs

The repository includes:

- Cleaned dataset
- Encoded dataset
- Scaled dataset
- Training and testing datasets
- Scaled training and testing datasets
- Clustered dataset
- K-Means trained model
- Visualisation figures
- Supporting documentation

---

## Software Requirements

- Python 3.x
- Jupyter Notebook

### Python Libraries

- pandas
- numpy
- matplotlib
- scikit-learn
- joblib

Install dependencies using:

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

---

## Running the Project

1. Clone the repository.

```bash
git clone <repository-link>
```

2. Open the project folder.

3. Launch Jupyter Notebook.

```bash
jupyter notebook
```

4. Open:

```
script.ipynb
```

5. Run all cells in sequence.

---

## Key Results

- Successfully prepared the telecom customer dataset for machine learning.
- Applied feature scaling to improve model performance.
- Identified the optimal number of customer clusters using the Elbow Method and Silhouette Score.
- Trained a K-Means clustering model.
- Visualised customer segments using Principal Component Analysis (PCA).
- Generated actionable business insights for customer retention.

---

## Future Work

Stage 3 of the project will build on this work by developing an Artificial Neural Network (ANN) to predict customer churn using the prepared dataset.

---

## Author

Prepared by the Stage 2 Project Team as part of the ACS Work Integrated Learning (WIL) Customer Churn Prediction Project.

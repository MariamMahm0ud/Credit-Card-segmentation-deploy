# Credit Card Clustering Segmentation

## Overview

The **Credit Card Clustering Segmentation** project aims to analyze and segment credit card customers based on their spending and payment behaviors. By applying machine learning techniques, this project classifies customers into distinct clusters to uncover patterns and insights that can guide targeted marketing strategies, credit management, and customer service improvements.

## Data
-you can see the data in kaggle : 
<a href="https://www.kaggle.com/datasets/arjunbhasin2013/ccdata">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png" alt="Kaggle" width="50"/>
</a>

The dataset used in this project is the **Credit Card Customer Data**, which includes a range of features related to customer credit card usage. The key features in the dataset are:

- **BALANCE**: The balance amount on the credit card.
- **PURCHASES**: Total purchases made with the credit card.
- **INSTALLMENTS_PURCHASES**: Purchases made with installment payments.
- **CASH_ADVANCE**: Amount of cash advances taken.
- **CREDIT_LIMIT**: The credit limit of the card.
- **PAYMENTS**: Total payments made towards the credit card balance.
- **MINIMUM_PAYMENTS**: Minimum payments made.
- **CASH_ADVANCE_TRX**: Number of cash advance transactions.
- **PURCHASES_TRX**: Number of purchase transactions.

## Project Structure

- **`app.py`**: The main Streamlit application script that provides an interactive interface for the analysis and visualization of the data.
- **`requirements.txt`**: Lists all the Python libraries required for the project.
- **`model.pkl`**: Serialized machine learning model used for clustering.
- **`clustering.py`**: Contains the functions for hierarchical clustering.
- **`preprocessing.py`**: Includes data preprocessing functions.
- **`analysis.py`**: Functions for analyzing clustering results.
- **`visualisations.py`**: Contains visualization functions for different analyses.
- **`visual2.py`**: Additional visualization functions for cluster analysis.
- **`README.md`**: This file, providing an overview of the project.

## Deployed Project

You can interact with the deployed application.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mariam-credit-card-segmentation-deploy.streamlit.app/)

## How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MariamMahmoud/Credit-Card-segmentation-deploy.git
   cd Credit-Card-segmentation-deploy
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run streamlit_app.py
   ```

## Features

- **Clustering Analysis**: Apply hierarchical clustering to segment customers.
- **Visualizations**: Includes t-SNE visualizations and cluster-specific histograms.
- **Business Insights**: Provides detailed business analysis for each customer segment.

## Conclusion

The Credit Card Clustering Segmentation project successfully segments credit card customers into meaningful clusters, offering valuable insights into their spending and payment behaviors. By leveraging hierarchical clustering and advanced visualization techniques, businesses can better understand customer segments and tailor their marketing strategies, credit policies, and customer service to address the specific needs of each segment. The interactive Streamlit application provides an accessible and user-friendly platform to explore these insights and make data-driven decisions.





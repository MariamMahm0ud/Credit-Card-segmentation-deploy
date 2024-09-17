import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

def plot_cluster_histograms(df_clustered, columns_of_interest):
    for column in columns_of_interest:
        plt.figure(figsize=(15, 5))
        for cluster_label in df_clustered['hi_cluster_labels'].unique():
            cluster_data = df_clustered[df_clustered['hi_cluster_labels'] == cluster_label]
            plt.subplot(1, len(df_clustered['hi_cluster_labels'].unique()), cluster_label + 1)
            sns.histplot(cluster_data[column], bins=20, kde=False, color='skyblue')
            mean_value = cluster_data[column].mean()
            median_value = cluster_data[column].median()
            plt.axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
            plt.axvline(median_value, color='green', linestyle='--', label=f'Median: {median_value:.2f}')
            plt.title(f'Cluster {cluster_label}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.legend()
        plt.tight_layout()
        st.pyplot(plt.gcf())

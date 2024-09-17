from preprocessing import load_data, preprocess_data, apply_log_transformation
from clustering import plot_dendrogram, hierarchical_clustering, apply_tsne
from visualisations import plot_cluster_histograms
from analysis import cluster_analysis

def main():
    data_path = 'CC GENERAL.csv'
    df = load_data(data_path)
    
    # Preprocess the data
    df_preprocessed = preprocess_data(df)
    
    # Apply log transformation
    skewness_features = ['BALANCE', 'PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'CREDIT_LIMIT',
                         'PAYMENTS', 'MINIMUM_PAYMENTS', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX']
    df_preprocessed = apply_log_transformation(df_preprocessed, skewness_features)
    
    # t-SNE visualization
    apply_tsne(df_preprocessed, 't-SNE Visualization After Scaling')
    
    # Dendrogram and clustering
    plot_dendrogram(df_preprocessed)
    cluster_labels, silhouette_avg = hierarchical_clustering(df_preprocessed, 5)
    df_preprocessed['hi_cluster_labels'] = cluster_labels
    
    # Business analysis visualizations
    columns_of_interest = ['BALANCE', 'PURCHASES', 'CREDIT_LIMIT', 'PAYMENTS']
    plot_cluster_histograms(df_preprocessed, columns_of_interest)
    
    # Cluster analysis descriptions
    analysis = cluster_analysis()
    for cluster, desc in analysis.items():
        print(f"{cluster} Analysis:")
        for key, value in desc.items():
            print(f"{key}: {value}")
        print()

if __name__ == '__main__':
    main()

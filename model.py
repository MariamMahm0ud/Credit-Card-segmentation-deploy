from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_samples, silhouette_score
import pandas as pd
import pickle

def build_clustering_model(df, n_clusters=5):
    """Apply hierarchical clustering and calculate silhouette scores."""
    hierarchical_model = AgglomerativeClustering(n_clusters=n_clusters)
    cluster_labels = hierarchical_model.fit_predict(df)
    
    # Calculate silhouette scores
    hi_silhouette_scores = silhouette_samples(df, cluster_labels)
    hi_silhouette_avg = silhouette_score(df, cluster_labels)
    
    print(f"Silhouette Score for {n_clusters} clusters: {hi_silhouette_avg}")
    
    # Add cluster labels to the DataFrame
    df_with_clusters = df.copy()
    df_with_clusters['hi_cluster_labels'] = cluster_labels
    
    return hierarchical_model, df_with_clusters

if __name__ == "__main__":
    df = pd.read_csv("cleaned_data.csv")
    model, df_with_clusters = build_clustering_model(df)
    df_with_clusters.to_csv("clustered_data.csv", index=False)
    # Save model for deployment
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
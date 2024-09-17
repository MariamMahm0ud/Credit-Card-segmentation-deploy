import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from kneed import KneeLocator

'''def plot_elbow_method(df, max_clusters=10):
    sse = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df)
        sse.append(kmeans.inertia_)
    
    fig, ax = plt.subplots()
    ax.plot(range(1, max_clusters + 1), sse, marker='o')
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('SSE')
    ax.set_title('Elbow Method for Optimal Number of Clusters')
    return fig
'''

def plot_elbow_method(df, max_clusters=10, chosen_clusters=5):
    sse = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df)
        sse.append(kmeans.inertia_)
    
    fig, ax = plt.subplots()
    ax.plot(range(1, max_clusters + 1), sse, marker='o')
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('SSE')
    ax.set_title('Elbow Method for Optimal Number of Clusters')

    # Highlight the chosen number of clusters
    ax.axvline(chosen_clusters, color='red', linestyle='--', label=f'optimal number of clusters: {chosen_clusters}')
    ax.legend()

    return fig

def plot_dendrogram(df):
    mergings_c = shc.linkage(df, method="complete", metric='euclidean')
    fig, ax = plt.subplots(figsize=(10, 7))
    shc.dendrogram(mergings_c, ax=ax)
    ax.set_title('Dendrogram for Hierarchical Clustering')
    return fig

def hierarchical_clustering(df, n_clusters):
    hierarchical_model = AgglomerativeClustering(n_clusters=n_clusters)
    cluster_labels = hierarchical_model.fit_predict(df)
    silhouette_avg = silhouette_score(df, cluster_labels)
    return cluster_labels, silhouette_avg

def apply_tsne(df, title, cluster_labels=None):
    tsne = TSNE(n_components=2, perplexity=30, max_iter=300)
    tsne_data = tsne.fit_transform(df)
    fig, ax = plt.subplots(figsize=(10, 8))
    if cluster_labels is not None:
        scatter = ax.scatter(tsne_data[:, 0], tsne_data[:, 1], c=cluster_labels, cmap='viridis')
        legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
        ax.add_artist(legend1)
    else:
        ax.scatter(tsne_data[:, 0], tsne_data[:, 1])
    ax.set_title(title)
    ax.grid(True)
    return fig

def apply_tsne2(df, title, label_column):
    
    
    # Apply t-SNE to the data excluding the label_column
    tsne = TSNE(n_components=2, random_state=42)
    tsne_results = tsne.fit_transform(df.drop(columns=[label_column]))  # Drop the cluster labels for t-SNE

    # Create a DataFrame for plotting
    tsne_df = pd.DataFrame(tsne_results, columns=['TSNE1', 'TSNE2'])
    tsne_df['Cluster'] = df[label_column].values  # Add the cluster labels back for coloring

    # Plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TSNE1', y='TSNE2', hue='Cluster', palette='tab10', data=tsne_df, legend="full")
    plt.title(title)
    plt.legend(title='Cluster')
    return plt.gcf()  # Returns the figure for Streamlit to display


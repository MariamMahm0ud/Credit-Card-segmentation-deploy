import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st

'''def plot_custom_histograms(df):
    columns = ["BALANCE", "PURCHASES", "CREDIT_LIMIT", "PAYMENTS"]

    for col in columns:
        plt.figure(figsize=(10, 5))

        # Dynamically calculate bins
        min_val = df[col].min()
        max_val = df[col].max()
        bins = np.linspace(min_val, max_val, 20)

        sns.histplot(data=df, x=col, bins=bins, kde=True)

        # Calculate percentage for each bin
        bin_counts = df[col].value_counts(bins=bins, normalize=True).sort_index()
        for j, count in enumerate(bin_counts):
            plt.text(
                bin_counts.index[j].mid,
                count,
                f'{count:.1%}',
                ha='center',
                va='bottom'
            )

        plt.xticks(bins)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Percentage')
        plt.tight_layout()
        st.pyplot(plt.gcf())  # Use st.pyplot() instead of plt.show()




def plot_paired_histograms(df, column_pairs, bins_list, insights_list):
    num_pairs = len(column_pairs)
    
    # Ensure bins_list and insights_list have the same length as column_pairs
    if len(bins_list) != num_pairs or len(insights_list) != num_pairs:
        raise ValueError("Length of bins_list and insights_list must match number of column pairs.")
    
    for i, (col1, col2) in enumerate(column_pairs):
        # Ensure bins are sorted and unique
        bins_col1 = np.unique(bins_list[i][0])
        bins_col2 = np.unique(bins_list[i][1])
        
        # Create and display histogram for the first column
        plt.figure(figsize=(12, 5))
        sns.histplot(data=df, x=col1, bins=bins_col1)
        plt.title(f'Histogram of {col1}')
        plt.xlabel(col1)
        plt.ylabel('Frequency')
        plt.xticks(bins_col1)
        # Add percentage annotations
        total_count = len(df)
        patches = plt.gca().patches
        for patch in patches:
            x = patch.get_x() + patch.get_width() / 2
            y = patch.get_height()
            percentage = '{:.1f}%'.format(100 * (y / total_count))
            plt.annotate(percentage, (x, y), ha='center', va='bottom')
        
        st.pyplot(plt.gcf())
        plt.close()

        # Create and display histogram for the second column
        plt.figure(figsize=(12, 5))
        sns.histplot(data=df, x=col2, bins=bins_col2)
        plt.title(f'Histogram of {col2}')
        plt.xlabel(col2)
        plt.ylabel('Frequency')
        plt.xticks(bins_col2)
        # Add percentage annotations
        patches = plt.gca().patches
        for patch in patches:
            x = patch.get_x() + patch.get_width() / 2
            y = patch.get_height()
            percentage = '{:.1f}%'.format(100 * (y / total_count))
            plt.annotate(percentage, (x, y), ha='center', va='bottom')
        
        st.pyplot(plt.gcf())
        plt.close()
        
        # Add insights for each histogram
        st.write(insights_list[i])

def plot_cluster_histograms2(df_clustered, columns_of_interest, n_clusters):
    for column in columns_of_interest:
        plt.figure(figsize=(10, 6))
        ax = plt.gca()

        for cluster_label, color in zip(df_clustered['hi_cluster_labels'].unique(), sns.color_palette('colorblind', n_clusters)):
            cluster_data = df_clustered[df_clustered['hi_cluster_labels'] == cluster_label]
            sns.histplot(cluster_data[column], bins=20, kde=False, color=color, label=f'Cluster {cluster_label}', ax=ax)

        plt.xlabel(column)
        plt.ylabel('Count')
        plt.title(f'Histogram of {column} for Each Cluster')
        plt.legend(title='Cluster')
        plt.tight_layout()
        st.pyplot(plt.gcf())
'''
def plot_custom_histograms(df):
    columns = ["BALANCE", "PURCHASES", "CREDIT_LIMIT", "PAYMENTS"]

    for col in columns:
        plt.figure(figsize=(10, 5))

        # Dynamically calculate bins
        min_val = df[col].min()
        max_val = df[col].max()
        bins = np.linspace(min_val, max_val, 20)

        sns.histplot(data=df, x=col, bins=bins, kde=False)  # KDE removed as per context

        # Calculate percentage for each bin
        bin_counts = df[col].value_counts(bins=bins, normalize=True).sort_index()
        for j, count in enumerate(bin_counts):
            plt.text(
                bin_counts.index[j].mid,
                count,
                f'{count:.1%}',
                ha='center',
                va='bottom'
            )

        plt.xticks(bins)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Percentage')
        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.close()  # Close the figure to avoid memory buildup

'''
# Paired histograms plotting
def plot_paired_histograms(df, column_pairs, bins_list, insights_list, rotation_angle=45):
    num_pairs = len(column_pairs)
    
    # Ensure bins_list and insights_list have the same length as column_pairs
    if len(bins_list) != num_pairs or len(insights_list) != num_pairs:
        raise ValueError("Length of bins_list and insights_list must match number of column pairs.")
    
    for i, (col1, col2) in enumerate(column_pairs):
        # Ensure bins are sorted and unique
        bins_col1 = np.unique(bins_list[i][0])
        bins_col2 = np.unique(bins_list[i][1])
        
        # Plot histogram for the first column
        plt.figure(figsize=(12, 5))
        sns.histplot(data=df, x=col1, bins=bins_col1)
        plt.title(f'Histogram of {col1}')
        plt.xlabel(col1)
        plt.ylabel('Frequency')
        
        # Rotate the x-axis labels
        plt.xticks(rotation=rotation_angle)  # Rotate x-axis labels by 45 degrees (or whatever value you want)
        
        # Add percentage annotations
        total_count = len(df)
        patches = plt.gca().patches
        for patch in patches:
            x = patch.get_x() + patch.get_width() / 2
            y = patch.get_height()
            percentage = '{:.1f}%'.format(100 * (y / total_count))
            plt.annotate(percentage, (x, y), ha='center', va='bottom')
        
        st.pyplot(plt.gcf())
        plt.close()

        # Plot histogram for the second column
        plt.figure(figsize=(12, 5))
        sns.histplot(data=df, x=col2, bins=bins_col2)
        plt.title(f'Histogram of {col2}')
        plt.xlabel(col2)
        plt.ylabel('Frequency')
        
        # Rotate the x-axis labels
        plt.xticks(rotation=rotation_angle)  # Rotate x-axis labels by 45 degrees (or whatever value you want)
        
        # Add percentage annotations
        patches = plt.gca().patches
        for patch in patches:
            x = patch.get_x() + patch.get_width() / 2
            y = patch.get_height()
            percentage = '{:.1f}%'.format(100 * (y / total_count))
            plt.annotate(percentage, (x, y), ha='center', va='bottom')
        
        st.pyplot(plt.gcf())
        plt.close()
        
        # Add insights for each histogram
        st.write(insights_list[i])'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

def plot_paired_histograms(df, column_pairs, bins_list, insights_list, rotation_angle=45, num_xticks=25):
    num_pairs = len(column_pairs)
    
    # Ensure bins_list and insights_list have the same length as column_pairs
    if len(bins_list) != num_pairs or len(insights_list) != num_pairs:
        raise ValueError("Length of bins_list and insights_list must match number of column pairs.")
    
    for i, (col1, col2) in enumerate(column_pairs):
        # Ensure bins are sorted and unique
        bins_col1 = np.unique(bins_list[i][0])
        bins_col2 = np.unique(bins_list[i][1])
        
        # Plot histogram for the first column
        plt.figure(figsize=(12, 5))
        sns.histplot(data=df, x=col1, bins=bins_col1)
        plt.title(f'Histogram of {col1}')
        plt.xlabel(col1)
        plt.ylabel('Frequency')
        
        # Generate custom x-ticks with the desired number of ticks
        x_min, x_max = df[col1].min(), df[col1].max()
        xticks = np.linspace(x_min, x_max, num_xticks)  # Generate 10 x-axis ticks
        
        # Set the x-ticks and rotate them
        plt.xticks(xticks, rotation=rotation_angle)  # Rotate x-axis labels
        
        # Add percentage annotations
        total_count = len(df)
        patches = plt.gca().patches
        for patch in patches:
            x = patch.get_x() + patch.get_width() / 2
            y = patch.get_height()
            percentage = '{:.1f}%'.format(100 * (y / total_count))
            plt.annotate(percentage, (x, y), ha='center', va='bottom')
        
        st.pyplot(plt.gcf())
        plt.close()

        # Plot histogram for the second column
        plt.figure(figsize=(12, 5))
        sns.histplot(data=df, x=col2, bins=bins_col2)
        plt.title(f'Histogram of {col2}')
        plt.xlabel(col2)
        plt.ylabel('Frequency')
        
        # Generate custom x-ticks for the second column
        x_min, x_max = df[col2].min(), df[col2].max()
        xticks = np.linspace(x_min, x_max, num_xticks)  # Generate 10 x-axis ticks
        
        # Set the x-ticks and rotate them
        plt.xticks(xticks, rotation=rotation_angle)  # Rotate x-axis labels
        
        # Add percentage annotations
        patches = plt.gca().patches
        for patch in patches:
            x = patch.get_x() + patch.get_width() / 2
            y = patch.get_height()
            percentage = '{:.1f}%'.format(100 * (y / total_count))
            plt.annotate(percentage, (x, y), ha='center', va='bottom')
        
        st.pyplot(plt.gcf())
        plt.close()
        
        # Add insights for each histogram
        st.write(insights_list[i])


# Improved plot_cluster_histograms with proper memory management
def plot_cluster_histograms2(df_clustered, columns_of_interest):
    n_clusters = len(df_clustered['hi_cluster_labels'].unique())
    for column in columns_of_interest:
        plt.figure(figsize=(15, 5))
        for i, cluster_label in enumerate(df_clustered['hi_cluster_labels'].unique()):
            cluster_data = df_clustered[df_clustered['hi_cluster_labels'] == cluster_label]
            plt.subplot(1, n_clusters, i + 1)
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
        plt.close()  # Close the figure to free memory
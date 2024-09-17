import streamlit as st
from preprocessing import load_data, preprocess_data, apply_log_transformation
from clustering import hierarchical_clustering, apply_tsne, apply_tsne2 ,plot_dendrogram,plot_elbow_method
from visualisations import plot_cluster_histograms
from analysis import cluster_analysis
import pandas as pd
from visual2 import plot_custom_histograms, plot_paired_histograms,plot_cluster_histograms2
import numpy as np

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Streamlit App
def main():
    st.title("Credit Card Clustering segmentation")

    if st.session_state.logged_in:
        st.sidebar.title("Navigation")
        options = ["Dashboard", "Cluster Analysis"]
        choice = st.sidebar.selectbox("Select Option", options)

        if choice == "Dashboard":
            dashboard_page()
        elif choice == "Cluster Analysis":
            cluster_analysis_page()
    else:
        login_page()

def login_page():
    st.subheader("Login")
    
    # Simple login form
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type='password')
    
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.sidebar.success("Go to Dashboard for Analysis")
        else:
            st.error("Invalid Username or Password")


def dashboard_page():
    st.subheader("Dashboard")
    
    # File uploader to upload the CSV file
    file_path = 'CC GENERAL.csv'  
    
    try:
        df = pd.read_csv(file_path)
        
        st.success("Data loaded successfully!")
        
        # Proceed with preprocessing
        df_preprocessed = preprocess_data(df)
        
        # Apply log transformation to skewed features
        skewness_features = ['BALANCE', 'PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 
                             'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 
                             'CASH_ADVANCE_TRX', 'PURCHASES_TRX']
        df_preprocessed = apply_log_transformation(df_preprocessed, skewness_features)

        # Dropdown menu to select plot type
        st.write("### Select Visualization Type")
        plot_option = st.selectbox("Choose Plot Type", 
                                   ["t-SNE Visualization", 
                                    
                                    "exploration data analysis",
                                    ])

        if plot_option == "t-SNE Visualization":
            st.write("t-SNE Visualization of Data After Preprocessing")
            tsne_fig_preprocessed = apply_tsne(df_preprocessed, 't-SNE Visualization After Scaling')
            st.pyplot(tsne_fig_preprocessed)



        elif plot_option == "exploration data analysis":
            st.write("exploration data analysis")
            
            # Define important columns
            important_columns = [
                'BALANCE','BALANCE_FREQUENCY', 'PURCHASES','ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 
                'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'TENURE','PRC_FULL_PAYMENT'
            ]
            
            # Filter column pairs to include only important columns
            column_pairs = [
                ('BALANCE', 'BALANCE_FREQUENCY'),
                ('PURCHASES', 'ONEOFF_PURCHASES'),
                ('INSTALLMENTS_PURCHASES', 'CASH_ADVANCE'),
                ('PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY'),
                ('PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY'),
                
                ('CREDIT_LIMIT', 'PAYMENTS'),
                
                ('TENURE', 'PRC_FULL_PAYMENT')
            ]
            
            filtered_column_pairs = [
                (col1, col2) for col1, col2 in column_pairs 
                if col1 in important_columns and col2 in important_columns
            ]

            # Generate bins and insights dynamically
            bins_list = []
            insights_list = []
            
            for col1, col2 in filtered_column_pairs:
                min_col1, max_col1 = df[col1].min(), df[col1].max()
                min_col2, max_col2 = df[col2].min(), df[col2].max()
                bins_list.append([
                    np.linspace(min_col1, max_col1, 27),
                    np.linspace(min_col2, max_col2, 27)
                ])
                
                column_insights = {
                'BALANCE': "### Insights of Balance:\n1. Approximately 47% of accounts have balances up to 800 units, indicating a significant portion of customers maintain low balances.\n2. About 30% of accounts maintain balances ranging from 800 to 2300 units, suggesting a moderate level of credit utilization.\n3. The remaining accounts have balances exceeding 2300 units, which could indicate higher spending or less frequent payments.",
                'BALANCE_FREQUENCY': "### Insights of Balance Frequency:\n1. Approximately 69% of accounts have a high frequency of balance updates, with a frequency ranging from 0.99 to 1, reflecting active account management.",
                'PURCHASES': "### Insights of Purchases:\n1. Approximately 85% of accounts have purchase amounts ranging from 0 to 2000 units, indicating a majority of customers make low to moderate purchases.\n2. About 10% of accounts exhibit purchase amounts between 2000 and 4000 units, suggesting a smaller segment of higher spenders.\n3. A smaller proportion, around 3% of accounts, fall within the range of 4000 to 6000 units, representing a niche group of high spenders.\n4. The remaining accounts have purchase amounts exceeding 6000 units, indicating a very small group of very high spenders.",
                'ONEOFF_PURCHASES': "### Insights of One-Off Purchases:\n1. Approximately 89.7% of accounts demonstrate one-off purchases ranging from 0 to 1600 units, with the remaining 10.3% exceeding 1600 units, highlighting a preference for smaller, one-time purchases.",
                'INSTALLMENTS_PURCHASES': "### Insights of Installment Purchases:\n1. Approximately 85% of accounts exhibit installment purchase amounts ranging from 0 to 900 units, indicating a preference for smaller installment purchases.\n2. The remaining 15% have installment purchase amounts exceeding 900 units, suggesting a smaller segment of customers who prefer larger installment purchases.",
                'CASH_ADVANCE': "### Insights of Cash Advance Transactions:\n1. Most customers (82%) exhibit a reluctance to make frequent cash advance transactions, with amounts ranging from 0 to 1900 units, indicating a preference for other forms of credit.\n2. However, nearly all customers (95%) have engaged in cash advance transactions occasionally, with transaction counts ranging from 0 to 5800 units, suggesting that cash advances are used as a last resort.",
                'CREDIT_LIMIT': "### Insights of Credit Limits:\n1. A significant proportion (19%) of customers have credit limits between 2500 and 3700 units, indicating a preference for moderate credit limits.\n2. 34% of customers have limits between 50 and 2500 units, suggesting a cautious approach to credit.\n3. 30% of customers have limits between 3700 and 7500 units, indicating a segment of customers with higher credit needs.",
                'PAYMENTS': "### Insights of Payment Behavior:\n1. Nearly all customers (98%) have made total payment amounts under 10,000 units, reflecting responsible credit management practices and conservative payment behavior.\n2. Most customers have minimum payments below 15,000 units, indicating a tendency to manage credit card debt within reasonable limits.\n3. A majority of customers (75%) do not opt for full payments, preferring partial payments or revolving credit utilization, which could indicate a reliance on credit for cash flow management.",
                'TENURE': "### Insights of Tenure:\n1. A significant portion (84%) of customers have a credit card tenure of 12 months, indicating a common duration of credit card service and possibly reflecting the age of the customer base or the product lifecycle.",
                'PRC_FULL_PAYMENT': "### Insights of Full Payment Percentage:\n1. Approximately 66% of customers have a full payment percentage from 0 to 0.4, indicating that the majority of customers do not pay their full balance each month.\n2. The remaining customers exhibit full payment percentages ranging from 0.4 to 1, suggesting a smaller segment of customers who pay their full balance regularly."
                }
                insights_list.append(column_insights.get(col1, "No insights available") + "\n" + column_insights.get(col2, "No insights available"))

            # Dropdown menu to select a specific pair of columns
            selected_pair = st.selectbox("Select Column Pair to Plot", filtered_column_pairs)
            
            # Find the index of the selected pair
            selected_index = filtered_column_pairs.index(selected_pair)
            
            # Plot the selected pair
            plot_paired_histograms(df, [selected_pair], [bins_list[selected_index]], [insights_list[selected_index]])

        

    except FileNotFoundError:
        st.error("Data file not found. Please ensure the file path is correct.")
        


def cluster_analysis_page():
    st.subheader("Cluster Analysis")

    # File uploader for CSV
    file_path = 'CC GENERAL.csv'

    try:
        df = pd.read_csv(file_path)
        
        df_preprocessed = preprocess_data(df)

        # Apply log transformation to skewed features
        skewness_features = ['BALANCE', 'PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 
                             'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 
                             'CASH_ADVANCE_TRX', 'PURCHASES_TRX']
        df_preprocessed = apply_log_transformation(df_preprocessed, skewness_features)

        # Slider for number of clusters with unique key
        n_clusters = st.slider("Select Number of Clusters (the best case is 5)", 2, 10, 5, key="cluster_slider")

        # Apply hierarchical clustering
        cluster_labels, silhouette_avg = hierarchical_clustering(df_preprocessed, n_clusters)

        df_c = df.dropna().drop(columns=['CUST_ID', 'PURCHASES_INSTALLMENTS_FREQUENCY',
                                         'ONEOFF_PURCHASES', 'CASH_ADVANCE_FREQUENCY'])
        df_c['hi_cluster_labels'] = cluster_labels
        df_preprocessed['hi_cluster_labels'] = cluster_labels

        st.write(f"Silhouette Score: {silhouette_avg:.2f}")

        # Dropdown to select different analysis/visualization options with unique key
        analysis_options = ["Elbow Method","t-SNE Visualization","Dendrogram", "Cluster-Specific Histograms", "Cluster-Specific Business Analysis"]
        analysis_choice = st.selectbox("Choose the analysis or visualization you want to view", analysis_options, key="analysis_choice")

        # t-SNE Visualization after clustering
        if analysis_choice == "t-SNE Visualization":
            with st.expander("t-SNE Visualization of Clusters", expanded=True):
                st.write("### t-SNE Visualization of Clusters")
                tsne_fig_clusters = apply_tsne2(df_preprocessed, 't-SNE Visualization of Clusters', label_column='hi_cluster_labels')
                st.pyplot(tsne_fig_clusters)
        elif analysis_choice == "Dendrogram":
            with st.expander("Dendrogram for Hierarchical Clustering", expanded=True):
                st.write("### Dendrogram for Hierarchical Clustering")

                fig = plot_dendrogram(df_preprocessed)
                st.pyplot(fig)
        elif analysis_choice == "Elbow Method":
            with st.expander("Elbow Method for Optimal Number of Clusters", expanded=True):
                st.write("### Elbow Method for Optimal Number of Clusters")
                fig = plot_elbow_method(df_preprocessed, chosen_clusters=5)
                st.pyplot(fig)



        # Cluster-Specific Histograms
        elif analysis_choice == "Cluster-Specific Histograms":
            with st.expander("Cluster-Specific Histograms", expanded=True):
                st.write("### Cluster-Specific Histograms")
                columns_of_interest = ['BALANCE', 'PURCHASES', 'CREDIT_LIMIT', 'PAYMENTS']
                plot_cluster_histograms2(df_c, columns_of_interest)

        # Cluster-Specific Business Analysis
        elif analysis_choice == "Cluster-Specific Business Analysis":
            with st.expander("Cluster-Specific Business Analysis", expanded=True):
                st.write("### Cluster-Specific Business Analysis (for best case 5 clusters)")
                analysis = cluster_analysis()
                for cluster, details in analysis.items():
                    st.write(f"#### {cluster}")
                    for key, value in details.items():
                        st.write(f"- **{key}**: {value}")
                
                business_analysis = {
                    0: "Cluster 0: This cluster comprises customers with moderate balances and a balanced approach to both purchases and payments. Their behavior suggests financial stability and consistent credit management, with a focus on maintaining low-risk profiles.",
                    1: "Cluster 1: Customers in this cluster show low balances but demonstrate responsible credit use, marked by moderate purchases and regular payments. They maintain good credit health, possibly avoiding high debt while utilizing credit wisely.",
                    2: "These customers tend to have high balances and rely heavily on cash advances rather than purchases. This suggests a preference for liquidity through credit lines, possibly indicating short-term financial pressure or strategic use of credit for non-consumer spending.",
                    3: "This cluster is characterized by high balances and moderate purchasing activity, paired with frequent cash advances and high credit limits. These customers may be leveraging credit for both consumption and liquidity, reflecting a more aggressive credit utilization strategy.",
                    4: "Customers here maintain moderate to high balances, making fewer purchases but frequently using cash advances. They may rely on credit for liquidity needs, signaling either high consumption behavior or a preference for flexible credit usage without large purchases."
                }
                for cluster, description in business_analysis.items():
                    st.write('conclusion analysis of cluster')
                    st.write(f"#### Cluster {cluster}")
                    st.write(description)


    except FileNotFoundError:
        st.error("Data file not found. Please ensure the file path is correct.")

if __name__ == "__main__":
    main()

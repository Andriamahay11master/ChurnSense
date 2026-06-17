import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(file_path):
    """Perform exploratory data analysis on the dataset."""
    # Load the dataset
    df = pd.read_csv(file_path)

    # Display basic information about the dataset
    print("Dataset Information:")
    print(df.info())
    print("\nDataset Description:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Visualize the distribution of the target variable (example: 'Churn')
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Churn', data=df)
    plt.title('Distribution of Churn')
    plt.show()

    # Visualize correlations between numerical features
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

if __name__ == "__main__":    # Example usage
    perform_eda('data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')
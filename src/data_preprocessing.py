import pandas as pd

def preprocess_data(file_path):
    """Preprocess the dataset for machine learning."""
    # Load the dataset
    df = pd.read_csv(file_path)

    # Handle missing values (example: fill with mean)
    df.fillna(df.mean(), inplace=True)

    # Encode categorical variables (example: one-hot encoding)
    df = pd.get_dummies(df, drop_first=True)

    # Normalize numerical features (example: min-max scaling)
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = (df[numerical_cols] - df[numerical_cols].min()) / (df[numerical_cols].max() - df[numerical_cols].min())

    return df
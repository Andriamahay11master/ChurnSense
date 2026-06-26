import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

def train_model_logistic_regression(df, target_column):
    """Train a machine learning model on the dataset."""
    # Split the dataset into features and target variable
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model (example: Logistic Regression)
    model = LogisticRegression(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    auc_score = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC AUC Score: {auc_score:.2f}")

    # Plot ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

    return model, fpr, tpr, auc_score


def train_model_random_forest(df, target_column):
    """Train a machine learning model on the dataset."""
    # Split the dataset into features and target variable
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model (example: Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    auc_score = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC AUC Score: {auc_score:.2f}")

    # Plot ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    
    return model, fpr, tpr, auc_score    

def train_model_xgboost(df, target_column):
    """Train a machine learning model on the dataset."""
    import xgboost as xgb

    # Split the dataset into features and target variable
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model (example: XGBoost)
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    auc_score = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC AUC Score: {auc_score:.2f}")

    # Plot ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    
    return model, fpr, tpr, auc_score

def train_model(df, target_column, model_type='logistic_regression'):
    """Train a machine learning model on the dataset."""
    if model_type == 'logistic_regression':
        return train_model_logistic_regression(df, target_column)
    elif model_type == 'random_forest':
        return train_model_random_forest(df, target_column)
    elif model_type == 'xgboost':
        return train_model_xgboost(df, target_column)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

def save_model(model, model_type='logistic_regression'):
    """Save the trained model to a file."""
    if model_type == 'logistic_regression':
        model.save('models/logistic_regression_model.joblib')
    elif model_type == 'random_forest':
        model.save('models/random_forest_model.joblib')
    elif model_type == 'xgboost':
        model.save('models/xgboost_model.joblib')
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

if __name__ == "__main__":    # Example usage
    # Load the preprocessed dataset
    df = pd.read_csv('data/processed/processed_data.csv')
    
    # Train the model and evaluate
    model, fpr, tpr, auc_score = train_model(df, target_column='Churn', model_type='random_forest')
    
    print(f"Model trained. ROC AUC Score: {auc_score:.2f}")
    save_model(model, model_type='random_forest')
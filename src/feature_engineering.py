import pandas as pd
import numpy as np

def calculate_age(birthdate):
    today = pd.to_datetime('today')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def feature_engineering(df):
    df['Age'] = df['customerID'].map(lambda x: calculate_age(df.loc[df['customerID'] == x, 'SeniorCitizen'].iloc[0]))
    df['TotalCharges'] = df['MonthlyCharges'] * df['tenure']
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df
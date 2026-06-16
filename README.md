# ChurnSense: Customer Churn Analysis & Prediction

**_Overview_**

ChurnSense is an end-to-end data analytics project focused on understanding customer churn behavior and identifying the factors that contribute to customer attrition. Using data analysis, SQL queries, interactive dashboards, and machine learning techniques, this project provides actionable insights that can help businesses improve customer retention and reduce churn rates.

# Business Problem

Customer churn is one of the most significant challenges faced by subscription-based businesses. Acquiring new customers is often more expensive than retaining existing ones. Understanding why customers leave can help organizations develop effective retention strategies and improve long-term profitability.

This project aims to analyze customer behavior and identify patterns associated with churn.

# Objectives

- Analyze customer demographics and subscription characteristics.
- Identify key factors influencing customer churn.
- Perform exploratory data analysis (EDA) to uncover trends and patterns.
- Generate business insights using SQL queries.
- Create interactive dashboards for stakeholder reporting.
- Build machine learning models to predict customer churn.
- Provide actionable recommendations to improve customer retention.

# Dataset

This project uses the IBM Telco Customer Churn dataset, which contains customer demographic information, account details, subscribed services, billing information, and churn status.

_Features_

| Category                   | Examples                        |
| -------------------------- | ------------------------------- |
| Customer Information       | Gender, Senior Citizen, Partner |
| Account Information Tenure | Contract Type                   |
| Services                   | Internet Service, Phone Service |
| Billing Information        | Monthly Charges, Total Charges  |
| Target                     | Churn                           |

_Target Variable_

Churn = Yes → Customer left the company.
Churn = No → Customer remained with the company.

# Project Structure

```
churnsense/
├── 📁data/
├── 📁notebooks/
├── 📁sql/
├── 📁dashboard/
├── 📁src/
├── 📁reports/
├── 📁images/
├── 📁models/
├── requirements.txt
├── README.md
└── .gitignore
```

# Project Workflow

Data Collection
↓
Data Understanding
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
SQL Analysis
↓
Dashboard Development
↓
Machine Learning
↓
Business Recommendations

# Tools & Technologies

**Programming**

- Python
- SQL

**Python Libraries**

- Pandas
- NumPy
- Matplotlib
- Scikit-learn

**Data Visualization**

- Power BI

**Database**

- PostgreSQL

**Version Control**

- Git
- GitHub

# Exploratory Data Analysis

The EDA phase focuses on answering key business questions such as:

- What is the overall churn rate?
- Which customer segments are more likely to churn?
- How does contract type influence churn?
- Does customer tenure impact retention?
- How do monthly charges affect churn behavior?
- Which services are associated with higher churn rates?

# SQL Analysis

SQL is used to extract business insights from the dataset, including:

- Churn rate by contract type
- Churn rate by payment method
- Customer distribution across services
- Revenue analysis
- High-risk customer segments

# Dashboard

The Power BI dashboard provides interactive visualizations and KPIs, including:

**Key Metrics**

- Total Customers
- Active Customers
- Churned Customers
- Churn Rate
- Average Monthly Charges

**Visualizations**

- Churn by Contract Type
- Churn by Internet Service
- Churn by Payment Method
- Customer Tenure Analysis
- Revenue and Churn Trends

# Machine Learning

The project includes predictive modeling to estimate customer churn probability.

**Models**

- Logistic Regression
- Random Forest

**Evaluation Metrics**

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

# Key Findings

_To be completed after analysis._

Example findings:

- Month-to-month customers exhibit the highest churn rates.
- Customers with shorter tenure are more likely to leave.
- Higher monthly charges are associated with increased churn risk.
- Contract type is one of the strongest predictors of churn.

# Business Recommendations

_To be completed after analysis._

Potential recommendations:

- Offer incentives for long-term contracts.
- Improve onboarding for new customers.
- Develop targeted retention campaigns for high-risk customers.
- Review pricing strategies for customer segments with high churn rates.

# Future Improvements

- Deploy a churn prediction web application.
- Integrate real-time customer monitoring.
- Implement automated churn alerts.
- Compare additional machine learning models such as XGBoost and LightGBM.

# Author

**Henikaja Andriamahay IRIMANANA**

MSc Artificial Intelligence with Machine Learning <br\>
Front-End Developer & Data Analytics Enthusiast

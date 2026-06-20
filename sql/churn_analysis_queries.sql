/* Churn Analysis Queries */
-- Churn rate by contract type
SELECT contract, COUNT(*) AS total_customers, SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers, SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) AS churn_rate
FROM churnsense
GROUP BY contract;

-- Churn rate by contract type and gender
SELECT contract, gender, COUNT(*) AS total_customers, SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers, SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) AS churn_rate
FROM churnsense
GROUP BY contract, gender;
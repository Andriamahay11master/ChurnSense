/* Database Schema */
CREATE TABLE churnsense (
    customer_id INT PRIMARY KEY,
    contract VARCHAR(255),
    gender VARCHAR(255),
    payment_method VARCHAR(255),
    internet_service VARCHAR(255),
    churn VARCHAR(255)
);

CREATE TABLE churnsense_test (
    customer_id INT PRIMARY KEY,
    contract VARCHAR(255),
    gender VARCHAR(255),
    payment_method VARCHAR(255),
    internet_service VARCHAR(255),
    churn VARCHAR(255)
);
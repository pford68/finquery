DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounting;

CREATE TABLE transactions(
   id VARCHAR(255) NOT NULL,
   date DATE,
   customer_id INT,
   amount decimal,
   type VARCHAR(255),
   description VARCHAR(255),
   PRIMARY KEY (id)
);

CREATE TABLE accounting(
   transaction_id VARCHAR(255) NOT NULL,
   date DATE,
   account_number INT,
   type VARCHAR(255),
   amount DECIMAL,
   currency VARCHAR(255),
   counterparty VARCHAR(255),
   category VARCHAR(255),
   payment_method VARCHAR(255),
   risk_incident INT,
   risk_type VARCHAR(255),
   incident_severity VARCHAR(255),
   error_code VARCHAR(255),
   user_id VARCHAR(255),
   system_latency DECIMAL,
   login_frequency INT,
   failed_attempts INT,
   ip_region VARCHAR(255),
   PRIMARY KEY (transaction_id)
);

LOAD DATA INFILE
  '/Users/philipford/Documents/Work/ProjetUp_IK/FinQuery/data/financial_transactions.csv'
  INTO TABLE transactions 
  fields terminated by ','
  lines terminated BY '\n'
  IGNORE 1 LINES;

LOAD DATA INFILE
  '/Users/philipford/Documents/Work/ProjetUp_IK/FinQuery/data/accounting_dataset.csv'
  INTO TABLE accounting 
  fields terminated by ','
  OPTIONALLY ENCLOSED BY '"'
  lines terminated BY '\n'
  IGNORE 1 LINES;

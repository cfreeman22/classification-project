# TELCO Classification Project

#  Why are Telco customers churning?

### By Christian Freeman 2021-11-25



## Project Planning

Understanding consumer behavior can quite chanlenging,  especially when the product we offer our customers is a service rather than a tangible physical products. In the case of Telco, in order to have a clear picture of customer churn, I will perform the following:
- Acquire the telco data from using acquire.py.
- Prepare the data using prepare.py
- Explore Data analysis
- Model building and Evaluation
- Deliver pressentation and recommendations 

## Data Dictionary 

|Continuous Features  |    Description                                                 |Data Type|
|---------------------|----------------------------------------------------------------|---------|
|monthly_charges      |How much a customer pays per month in dollars                   |float64  |
|total_charges        |How much a customer has paid over the course of their tenure    |float64  |
|tenure               |how many months the customer has been with the company          |int64    |

|Categorical Features |    Description                                                 |Data Type|
|---------------------|----------------------------------------------------------------|---------|
|senior_citizen       |indicates if the customer is a senior citizen                   |int64    |
|partner              |indicates if the customer has a partner                         |int64    |
|dependents           |indicates if the customer has dependents                        |int64    |
|phone_service        |indicates if the customer has phone service with Telco          |int64    |
|multiple_lines       |indicates if the customer with phone service has multiple lines |int64    |
|online_security      |indicates if the customer has online security services          |int 64   |
|online_backup        |indicates if the customer has online backup services            |int64    |
|device_protection    |indicates if the customer has device protection services        |int64    |
|tech_support         |indicates if the customer has tech support services             |int64    |
|streaming_tv         |indicates if the customer has tv streaming services             |int64    |
|streaming_movies     |indicates if the customer has movie streaming services          |int64    |
|payment_type         |indicates the type of payment method a customer is using        |int64    |
|internet_service_type|indicates which internet service (if any) the customer has      |int64    |
|gender               |indicates the the customers' gender identity                    |uint8    |
|contract_type        |indicates the type of contract the customer has with Telco      |int64    |

|Target               |   Description                                                  |Data Type|
|---------------------|----------------------------------------------------------------|---------|
|churn                |indicates whether or not a customer churned                     |int64    |

|Other                |   Description                                                  |Data Type|
|---------------------|----------------------------------------------------------------|---------|
|customer_id          |customer id number                                              |object   |
 
 ##  Goals and summary

My goal in this project is to: 
- Identify the characteristics of customers who are more likely to churn, and the potential reasons for this behavior.
- Build a ML model to predict customer churn
- So that recommendations are made based on the findings to help telco minimize the churn rate and maximize customer retention and revenue.
- Recommendations will be made based on the findings.
- I will be using Python, Pandas, Matplot, Seaborn, and Scikit-Learn libraries to analyse and create ML classification model.


## Objectives

- Create Documentation for code, and all processes involved in the project such as 
data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation. 

- Document key findings, and takeaways in a Jupyter Notebook report.

- Create modules (acquire.py, prepare.py) that simplfy and automate data acquisition and preparation proccesses.

- Use classification techniques to build a model that predict customer churn

- Deliver a 5 minute workthrough presentation  using jupyter Notebook appropriate for target audience.

- Answer panel questions about the process, code, findings, key takeaways, and model.


## Audience
- Telco management


## Initial Questions

Why do customers churn?

Which Category or subCategory churn the most?

What service do they use?

What payment methods do they use?

Can we predict churn?



## Hypotheses 


- H0:  customer churn is independent of which payment type they use

- Ha:  customer churn has a dependent of which payment type they use 


- H0:  customer churn is independent of which contract type they have
- Ha:  customer churn has a dependent of which contract type they have


## Key Findings

Continuing to dig deeper into the initial findings from the previous Telco churn project, we can now state that the payment method that a customer uses is not independent of churn

A customer's contract type and specific payment method are good indicators of churn.

Customers who were on month-to-month contracts were more likely to churn

Customers who use electronic checks as their payment method were more likely to churn.

Customers who use automatic payment methods are less likely to churn than those not on automatic payments

The Random Forest model was successful in predicting churn accuracy on TEST data with an accuracy of 0.80!

That is a higher than the baseline which was 0.73.


## Recommendations & Takeaways

Offer incentives to convert to automatic payment plans Offer incentives to convert month-to-month customers to longer term customers Find out more about electronic check customers to determine if there are issues causing their churn Next Steps Continue running more models changing the hyperparameters to get a better model of churn Group features together, such as month-to-month e-check customers who do not have partners or service types to run models on Send a survery to customers who churn to further understand their actual reason for leaving Fine tune the model by optimizing for precision or recall


## How to Recreate This Project
To recreate this project you will need the following files from this repository:

-  README.md
-  env file for you data base credentials to connect to the SQL database containing -  -  Telco data
-  acquire.py
-  prepare.py
-  explore.py
-  model.py
-  Final Telco Churn Project Notebook.ipynb

### Instructions:

Read the README.md
Download the aquire.py, prepare.py, explore.py and final_report.ipynb files into your working directory, or clone this repository
Add your own env file to your directory (user, password, host)
Run the Final Telco Churn Project Notebook.ipynb notebook





































# loan_predictor
## To predict the eligibility of loan for a customer.

A Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan.


Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers.

following are features:

Loan_ID : Unique Loan ID

Gender : Male/ Female

Married	Applicant married : (Y/N)

Dependents : Number of dependents

Education : Applicant Education (Graduate/ Under Graduate)

Self_Employed : Self employed (Y/N)

ApplicantIncome : Applicant income

CoapplicantIncome : Coapplicant income

LoanAmount : Loan amount in thousands

Loan_Amount_Term : Term of loan in months

Credit_History ; credit history meets guidelines

Property_Area : Urban/ Semi Urban/ Rural

Loan_Status	(Target) : Loan approved (Y/N)

# Project Steps

### 1. Problem Statement:
This model will predict customer eligibility for loan based on certain factors

### 2. Data Gathering:

You can download data [Click Here](https://www.kaggle.com/datasets/devzohaib/eligibility-prediction-for-loan/download?datasetVersionNumber=1)

### 3. EDA and Feature Engineering:

In this step,data is  analyze and investigate and summarize their main characteristics, 

1. Handling missing values

2. Checking for categorical data(Encoding require)

3. Feature transformation

4. Feature Scaling 

### 4. Feature Selection:
* The goal of feature selection techniques in machine learning is to find the best set of features that allows one to build optimized models of studied phenomena.

* Model performance improve.

* Model training time optimizes.

* Feature Selection:
    * Filter Method

    * Wrapper Method

    * Embedded Method

### 5. Model Training:
In this step Model is train using different machine learning techniques, here logistic regression is used.

### 6. Model Evalution:

To check model is performing well on training data set as well as testing data data we need evalate some metrics as follows,
* Confusion Matrix
* Classification report
* accuracy score
* roc curve

### 7. Web development Framework:
In this project flask method is used to write API's for the project so that user can interacte with help of html web to input the value and to get the output

### 8. Deployment on AWS: 
For public access we have used AWS service, so that anyone can access the website and can use to get the results.

# Important Files

1. interface.py :-

    In this file we have write the API's and by running this file you can start server.

2. util.py :-

    This file contains the basic function that will help to interface file to get the results

3. config.py :-

    * In this file you can change the file path for the pickle file and json file.
    * Also, you can change the port number according to the requirement

4. requirement.txt :-

    This file contain necessary libraries and its version, user need to install this libraries while running this project.

5. source.html :-

    This html file, contain website page coding.

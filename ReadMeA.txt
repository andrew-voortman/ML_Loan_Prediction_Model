# ML_Loan_Prediction_Model
By: Damien Crim, Grifin Racey, Andrew Voortman, Luke Payne, and Amanda Baynard

### Proposal/Ideation

Our end goal is to build a machine learning model that will find out which people are approved to get a loan or not based on our prediction (Loan_Status - Loan approved (Y/N)). The other following columns (below) will be factored in to determine if said people are approved or not.

### Data fetching/API integration

Kaggle.com "train_u6lujuX_CVtuZ9i.csv"

### Data Analysis
Numpy, Pandas, matplotlib, seaborn, sklearn, Tableau

Prediction dataset has:
    xx Factors
    xxx Samples

Descriptive Analysis
![Descriptive_Analysis](image.png)


Loan Data Factors: 
1 . Loan_ID- Unique Loan ID
2 . Gender - Male/ Female
3 . Married - Applicant married (Y/N)
4 . Dependents - Number of dependents
5 . Education - Applicant Education (Graduate/ Under Graduate)
6 . Self_Employed - Self employed (Y/N)
7 . ApplicantIncome - Applicant income
8 . CoapplicantIncome - Coapplicant income
9 . LoanAmount- Loan amount in thousands
10 . Loan_Amount_Term - Term of loan in months
11 . Credit_History - credit history meets guidelines
12 . Property_Area - Urban/ Semi Urban/ Rural
13 . Loan_Status - Loan approved (Y/N)

Filter out the "null values" for each of the categories that correlate to the loan status of "yes"


### Building the Machine Learning Model
Images of building code


### Testing
Simple Logistic Regression
    Accuracy: XX% for Training and xx% for Testing

Image of Logistic Regression Model

Logistic Regression with Standard Scaling and PCA
    Accuracy: XX% for Training and xx% for Testing

Image of Logistic Regression with Scaling

Simple Decision Tree Classifier
    Accuracy: XX% for Training and xx% for Testing for each depth

Image of Simple Decision Tree @ various max_depths

Test Data Predictions:
Remove nulls
Prediction table images

Testing Outcome
    Y: 
    N:

### Creating documentation
Tableau / ReadMe

Powerpoint

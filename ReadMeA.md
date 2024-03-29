# Loan Prediction Model

Our end goal is to build a machine learning model that will find out which people are approved to get a loan or not based on our prediction (Loan_Status - Loan approved (Y/N)). The other following columns (below) will be factored in to determine if said people are approved or not.


## Data Fetching/API integration/Processing

Data sets from Kaggle.com: 
- "train_u6lujuX_CVtuZ9i.csv"
- "test_Y3wMUE5_7gLdaTN.csv"

### Data Analysis

Numpy, Pandas, matplotlib, seaborn, sklearn, Tableau

Prediction dataset has:
    13 Factors
    614 Samples

Loan Data Factors: 
1. Loan_ID- Unique Loan ID
2. Gender - Male/ Female
3. Married - Applicant married (Y/N)
4. Dependents - Number of dependents
5. Education - Applicant Education (Graduate/ Under Graduate)
6. Self_Employed - Self employed (Y/N)
7. ApplicantIncome - Applicant income
8. CoapplicantIncome - Coapplicant income
9. LoanAmount- Loan amount in thousands
10. Loan_Amount_Term - Term of loan in months
11. Credit_History - credit history meets guidelines
12. Property_Area - Urban/ Semi Urban/ Rural
13. Loan_Status - Loan approved (Y/N)

Descriptive Analysis

![Descriptive Analysis](<Train Data Descriptive Analysis.png>)


Filter out the "null values" for each of the categories that correlate to the loan status of "yes"

![Null Values](<Null Values.png>)

##Reviewed for imbalanced dataset                                              

![Loan Status Balance](<Loan Status balance.png>)


#### How we changed the data to be balanced better:

Droping Loan_ID Column, ApplicantIncome and CoapplicantIncome (after combining incomes)
![Drop](<Drop Columns.png>)

Dropping all Null values for Gender and Married Columns                                                                                                             
![Null Removal](<Gender and Marrried Null Removal.png>)

Change Nulls to Not Self Employed for the Self_Employed Column                                                    
![Self Employed Null](<Self Employed Null Encoding.png>)

Combine ApplicantIncome and CoapplicantIncome                                                                    
![Combine Income](<Income Combination.png>)

Change Null to 360 for Loan_Amount_Term                                                            
![Loan Term Conversion](<360 Conversion.png>)

Update the Dependents Column with values                                                              
![Dependent Change](<Married with Dependents Null Change.png>)

Update LoanAmount and Credit_History columns with K Nearest Neighbor                                                                
![Loan Amount and Credit History Change](<Credit History and Loan Amount Change.png>)

#### Encode the data as numerical
Gender
- Female: 1
- Male/Other: 0

Marriage
- Marriage = Yes: 1
- Marriage = No: 0

Education
- Graduate: 1
- Not Graduate: 0

Self Employed
- Self Employed = Yes: 1
- Self Employed = No: 0

Dependents & Property Area
- Change type to Integer

    

## Building the Machine Learning Model

Decision Tree                                                                                               
![Decision Tree](image-4.png)

Neural Network                
3 Layers:                                                                                              
- ![3-Layer](image-2.png)

6 Layers:                                                                                                          
- ![6-Layer](image-3.png)

Logistic Regression                                                                                               
- Scikit:                                                                                                      
  ![Logistic Regression](image.png)                                                                    

- Pycaret:                                                                                               
 ![ROC Curve](image-1.png)                                                                             

Random Forest Classifier                                                                                    
- ![Random Forest](image-5.png)                                                                        


## Testing and Predictions

Decision Tree
    
    Accuracy: 76.67%

Neural Network
    
    3 Layer Accuracy: 76.67%
    6 Layer Accuracy: 64%

Logistic Regression
    
    Accuracy: 76% 

Random Forest Classifier
    
    Accuracy: 78.6%


## Authors

  - Damien Crim
  - Griffin Racey
  - Andrew Voortman
  - Luke Payne
  - Amanda Baynard

## Acknowledgments

  - Kaggle.com
  - Will and Erin
  - ChatGPT
  - Google

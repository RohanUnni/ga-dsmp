# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include= 'number')
print(numerical_var)
 





# code ends here


# --------------
# code starts here
banks=bank.drop(["Loan_ID"], axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
banks.isnull().values.any()
#code ends here




# --------------
# Code starts here



avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
print(avg_loan_amount)



# code ends here



# --------------
# code starts here




loan_approved_se=banks[(banks["Self_Employed"] == "Yes" ) & (banks["Loan_Status"] == "Y")].shape[0]

loan_approved_nse=banks[(banks["Self_Employed"] == "No" ) & (banks["Loan_Status"] == "Y")].shape[0]

percentage_se=(loan_approved_se/614)*100

percentage_nse=(loan_approved_nse/614)*100

# code ends here


# --------------
# code starts here



loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )


big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)
# code ends here


# --------------
# code starts here





loan_groupby=banks.groupby("Loan_Status")["ApplicantIncome","Credit_History"]
mean_values=loan_groupby.mean()





# code ends here



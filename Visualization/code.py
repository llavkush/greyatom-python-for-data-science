# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status= data["Loan_Status"].value_counts()
loan_status.plot(kind ="bar")


#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
# Label X-axes and Y-axes


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar')
plt.xlabel('Education Status')
plt.ylabel('Loan_Status')
# Rotate X-axes labels
plt.xticks(rotation=45)


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == ' Not Graduate']

data["LoanAmount"].plot(kind='density', label ='Graduate')
data['LoanAmount'].plot(kind='density', label ='Not Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3 , ncols = 1,figsize=(20,20))
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')
ax_3.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_3.set_title('Total Income')




data["TotalIncome"] = data["ApplicantIncome"] + data["CoapplicantIncome"]




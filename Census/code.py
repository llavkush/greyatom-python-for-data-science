# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
#Code starts here
census = np.concatenate((data, new_record), axis=0)
print(census.shape)


# --------------
#Code starts here
import numpy as np
age = census[:,0]
print(age)
max_age = age.max()
print(max)
min_age = age.min()
print(min)
age_mean = age.mean()

age_std = np.std(age)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)



print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)


race_list=[len_0, len_1,len_2, len_3, len_4]
minority_race=race_list.index(min(race_list))





# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]

print(senior_citizens)
working_hours_sum =senior_citizens.sum(axis=0)[6]

print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

#Creating an array based on 'education' column
high=census[census[:,1]>10]

#Finding the average pay
avg_pay_high=high[:,7].mean()

#Printing the average pay
print(avg_pay_high)

#Creating an array based on 'education' column
low=census[census[:,1]<=10]

#Finding the average pay
avg_pay_low=low[:,7].mean()

#Printing the average pay
print(avg_pay_low)
#Code ends here




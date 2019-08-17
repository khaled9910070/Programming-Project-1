import pandas as pd
import numpy as np
from statistics import mean


def withdrawn():
    dataA = pd.read_csv("studentInfo.csv")
    target_count = dataA['final_result'].value_counts()

    # print('Pass:', target_count[0])
    # print('Withdrawn:', target_count[1])
    # print('Fail:', target_count[2])
    # print('Distinction:', target_count[3])
    # Pass: 12361
    # Withdrawn: 10156
    # Fail: 7052
    # Distinction: 3024

    #weka stats
    #Code_Module AAA(126), BBB(2388), CCC(1975), DDD(2250), EEE(722),FFF(2403), GGG(292)
    #code_presentation 2013J(2369), 2014J(3826), 2013B(1348), 2014B(2613)
    #Gender F(4486), M(5670)
    #education ALevel(4030), lowerthanA(4620),HEqual(1283),NoQual(149),PostGrad(74)
    #age 35-55(2721), 0-35(7381), 55<= (54)
    #disability Y (1245), N(8911)

    a = dataA[dataA['final_result'] == 'Withdrawn']
    a = a.set_index('id_student')
    a.to_csv("withdrawnA.csv")

    print(a)


def withdrawnAssessment():
    dataA = pd.read_csv("assessments.csv")
    dataA = dataA.set_index('id_assessment','code_module')

    dataB = pd.read_csv("studentAssessment.csv")
    dataB = dataB.set_index('id_assessment','code_module')

    df_index = pd.merge(dataA, dataB, right_index=True, left_index=True)
    df_index = df_index.set_index(['id_student','code_module','code_presentation'])

    dataC = pd.read_csv("withdrawnA.csv")
    dataC = dataC.set_index(['id_student','code_module','code_presentation'])

    withdrawn_index = pd.merge(df_index, dataC, right_index=True, left_index=True)

# For loop it print all column names
#     for col in withdrawn_index.columns: 
#         print(col) 
# assessment_type, date,weight,date_submitted,is_banked,score,gender,region,highest_education,
# imd_band,age_band,num_of_prev_attempts,studied_credits,disability,final_result
# shows the columns of withdrawn index

#date – information about the final submission date of the assessment calculated as the number of days since the start of the module-presentation. 
#The starting date of the presentation has number 0 (zero).
#date_submitted – the date of student submission, measured as the number of days since the start of the module presentation.
#is_banked – a status flag indicating that the assessment result has been transferred from a previous presentation.

    assessmentWithdrawn =  withdrawn_index[['assessment_type','weight','date','date_submitted','score','final_result','is_banked','num_of_prev_attempts']]

    assessmentWithdrawn['date_diff'] = assessmentWithdrawn.apply(lambda row: row['date'] - row['date_submitted'], axis=1)
    #applys a lambda function to see how many days early or late the student submitted the assessent

    assessmentWithdrawn['score'].fillna(0, inplace=True)
    #replaces all null values in score with 0

    # value = assessmentWithdrawn.isnull().sum()
    # print(value)
    # checks for any null values in assessmentWithdrawn Dataframe

    print(assessmentWithdrawn)
    assessmentWithdrawn.to_csv("assessmentSubmitionWithdrawn.csv")




withdrawnAssessment()
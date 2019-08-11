import pandas as pd
import numpy as np

def cleand4():
    d4 = pd.read_csv("studentInfo.csv")
    value = d4.isnull().sum()
    newd4 = d4.dropna(how='any').shape
    #print(value)
    #1111 records missing for imd_band  
    missingValue = d4[(d4['imd_band'].isnull()) & (d4['final_result'] == 'Withdrawn')]
    #236 rows withdrawn + imd_band is null
    withdrawnStudent = d4[ d4['final_result'] == 'Withdrawn']
    newws = withdrawnStudent.dropna()
    #drops nan values from withdrawn student DF
    print(newws)
    #10,156 students have withdrawn from a certain class


def disabilityDataSet():
    #Hypothesis:
    # does having a disability a factor to the overall performance of a student in regards to their final result
    d4 = pd.read_csv("studentInfo.csv")
    d4 = d4.set_index(['code_module', 'region'])
    df = d4[(d4['disability']== 'Y')]
    #3164 students with a disability
    # looks at the number of students who pass/withdrawn/fail/distinction 

    studentResults = df[["id_student", "studied_credits", "final_result"]]
    studentResults = studentResults.sort_index()
    df1 = df['final_result'].value_counts()
    #counts the values of final_result 
    df2 = df.groupby('code_module')['final_result'].value_counts()
    #counts the values of final_result grouped by code_module
    df3 = df.groupby('studied_credits')['final_result'].value_counts()
    #counts the values of final_result grouped by studied_credits
    df4 = df.groupby('highest_education')['final_result'].value_counts()
    #counts the values of final result grouped by studied_credits
    df5 = df.groupby('gender')['final_result'].value_counts()
    #counts the values of final result grouped by gender
    df6 = df.groupby('age_band')['final_result'].value_counts()
    #counts the values of final result grouped by age
    df7 = df.groupby('num_of_prev_attempts')['final_result'].value_counts()
    #counts the values of final result grouped by prev_attempts 

    df8 = df.groupby('code_presentation')['final_result'].value_counts()
    # studentResults.to_csv('disabilityDataSet.csv')
    # writes dataframe into a csv file

   
    # print(studentResults)
    print(df8)
    
    


def regionDataSet():
    #Hypothesis:
    # Does the region the student lives in a factor on overall student performance 
    data = pd.read_csv("studentInfo.csv")
    data = data.set_index(['code_module', 'region'])
    df1 = data.groupby('region')['final_result'].value_counts()
    #Counts the number of pass/withdrawn/fail/Distinction by the region
    df2 = data.groupby('code_module')['final_result'].value_counts()
    #Counts final result value grouped by code_module
    df3 = data.groupby('studied_credits')['final_result'].value_counts()
    #Counts final result value grouped by studied_credits
    df4 = data.groupby('highest_education')['final_result'].value_counts()
    #Counts final result value grouped by highest_education
    df5 = data.groupby('gender')['final_result'].value_counts()
    #Counts final result value grouped by gender
    df6 = data.groupby('age_band')['final_result'].value_counts()
    #Counts final result value grouped by age
    df7 = data.groupby('num_of_prev_attempts')['final_result'].value_counts()
    #Counts final result value grouped by prev_attempts
    df8 = data.groupby('code_presentation')['final_result'].value_counts()
    #Counts final result value grouped by code_presentation

    # data = data.index
    studentResults = data[["id_student", "studied_credits", "final_result"]]
    studentResults = studentResults.sort_index()

    
    # studentResults.to_csv('regionDataSet.csv')
    # writes dataframe into a csv file
    print(df8)


regionDataSet()
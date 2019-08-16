import pandas as pd
import numpy as np
from statistics import mean

def vleName():
        data = pd.read_csv("vle.csv")
        data = data.set_index(['id_site','code_module','code_presentation'])
        #uses the vle.csv data set and makes the index of the dataset as above
        #the index will be used in a similar way as SQL PK
        data1 = pd.read_csv("studentVle.csv")
        data1 = data1.set_index(['id_site','code_module','code_presentation'])
        #uses the studentVle.csv data set and makes the index of the dataset as above
        #the index will be used in a similar way as SQL PK
        df_index = pd.merge(data, data1, right_index=True, left_index=True)
        # merges the data based on the index(similar to SQL join)
        #have 3 indexes will prevent repeated columns

        combinedVle = df_index.groupby(['id_student','code_module','id_site','activity_type']).agg({'sum_click': ['sum']})
        #the 4 index values help with showing the unique sum_click values based on the index
        #it also aggregates the values and finds the sum of sum_clicks for the entire day based on their activity type
        #went from 10mil records to 1.9mil

        combinedVleDate = df_index.groupby(['id_student','code_module','id_site','activity_type','date']).agg({'sum_click': ['sum']})
        #same as above but it has another index which is date
        #went from 10mil to 8mil records
        
        print(combinedVle)
        # combinedVle.to_csv('combinedVle.csv')
        # df = data.pivot_table(data, index=['id_site','code_module','activity_type']).head()



def studentResult():
        data = pd.read_csv("studentInfo.csv")
        data = data.set_index('id_student')

        data2 = pd.read_csv("combinedVle.csv")
        data2 = data2.set_index('id_student')
        #setting the index of the CSV files to id_Student

        df_index = pd.merge(data, data2, right_index=True, left_index=True)
        #merging the datasets on id_student
        
        # df = df_index.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])

        #the following code groups the merged data based on the code_module
        #The new data frame of the code_module is then used to create a pivot table
        #The index used in the pivot table allows to find specific data relating to student interaction to resources and their final_result
        #the pivot table is then sampled to count the values of final_result
        #avalue is buggy because its showing 3 columns all of the same value *needs to be fixed*
        a = df_index[df_index['code_module_x'] == 'AAA']
        aaa = a.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        
        b = df_index[df_index['code_module_x'] == 'BBB']
        bbb = b.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
     

        c = df_index[df_index['code_module_x'] == 'CCC']
        ccc = c.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
      

        d = df_index[df_index['code_module_x'] == 'DDD']
        ddd = d.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
      

        e = df_index[df_index['code_module_x'] == 'EEE']
        eee = e.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        

        f = df_index[df_index['code_module_x'] == 'FFF']
        fff = f.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])

        g = df_index[df_index['code_module_x'] == 'GGG']
        ggg = g.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])


        # df2.to_csv("vleResults.csv")
        # aaa.to_csv("codeModuleA.csv")
        # bbb.to_csv("codeModuleB.csv")
        # ccc.to_csv("codeModuleC.csv")
        # ddd.to_csv("codeModuleD.csv")
        # eee.to_csv("codeModuleE.csv")
        # fff.to_csv("codeModuleF.csv")
        # ggg.to_csv("codeModuleG.csv")
        #all of these are used to create the new csv files. only uncomment when you want to create the file

        print(cvalue)
        


def dataBalancing():
        dataA = pd.read_csv("CodeModuleResults/codeModuleA.csv")

        # target_count = dataA['final_result'].value_counts()
        # print('Pass:', target_count[0])
        # print('Withdrawn:', target_count[1])
        # print('Fail:', target_count[2])
        # print('Distinction:', target_count[3])

        # print('Proportion:', round(target_count[0]/target_count[3],2),':1')
        # #pass/distinction 9.0:1
        # print('Proportion:', round(target_count[1]/target_count[3],2),':1')
        # #withdrawn/distinction 1.71: 1
        # print('Proportion:', round(target_count[2]/target_count[3],2),':1')
        # #Fail/Distinction 1.08: 1

        #Uses the under-sampling method to even out the dataset
        #with the old dataset it was heavily infavor of students with a final_result of Pass
        #The lowest count of final_result is Distinction with 3724
        #The data was randomly resampled to 3724

        count_class_0, count_class_1,count_class_2, count_class_3 = dataA['final_result'].value_counts()
        passGrade = dataA[dataA['final_result'] == 'Pass']
        withdrawn = dataA[dataA['final_result'] == 'Withdrawn']
        fail = dataA[dataA['final_result'] == 'Fail']
        distinction = dataA[dataA['final_result'] == 'Distinction']
        #this sets the variables of pass/withdraw/fail/distinction
        pass_under = passGrade.sample(count_class_3)
        #this is where the data gets resampled to count_class_3 --> Distinction(3724)
        df_test_pass = pd.concat([pass_under, distinction], axis=0)

        withdrawn_under = withdrawn.sample(count_class_3)
        df_test_withdrawn = pd.concat([withdrawn_under, distinction], axis=0)

        fail_under = fail.sample(count_class_3)
        df_test_fail = pd.concat([fail_under,withdrawn_under,pass_under,distinction])
        #concatinates all the resampled data 
        df_test_fail.to_csv("sampleA.csv")
        #exported to CSV

        print('Random under-sampling:')
        print(df_test_fail)

       



dataBalancing()
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
        avalue = aaa.groupby('final_result').count()
        
        b = df_index[df_index['code_module_x'] == 'BBB']
        bbb = b.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        bvalue = bbb.groupby('final_result').count()

        c = df_index[df_index['code_module_x'] == 'CCC']
        ccc = c.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        cvalue = ccc.groupby('final_result').value_counts()

        d = df_index[df_index['code_module_x'] == 'DDD']
        ddd = d.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        dvalue = ddd.groupby('final_result').count()

        e = df_index[df_index['code_module_x'] == 'EEE']
        eee = e.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        evalue = eee.groupby('final_result').count()

        f = df_index[df_index['code_module_x'] == 'FFF']
        fff = f.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        fvalue = fff.groupby('final_result').count()

        g = df_index[df_index['code_module_x'] == 'GGG']
        ggg = g.pivot_table(df_index, index=['id_student', 'code_module_x' ,'code_presentation','final_result', 'activity_type','id_site'])
        gvalue = ggg.groupby('final_result').count()


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
        


studentResult()
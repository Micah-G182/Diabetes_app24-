import pandas as pd
d1 = pd.read_csv('Diabetes_data.csv')
d2 = d1.loc[(d1['Glucose']!=0)&(d1['BloodPressure']!=0)&(d1['SkinThickness']!=0)&(d1['Insulin']!=0)&(d1['BMI']!=0)]

d1['Glucose'].replace(0,d2['Glucose'].mean(), inplace=True)
d1['BloodPressure'].replace(0,d2['BloodPressure'].mean(), inplace=True)
d1['SkinThickness'].replace(0,d2['SkinThickness'].mean(), inplace=True)
d1['Insulin'].replace(0,d2['Insulin'].mean(), inplace=True)
d1['BMI'].replace(0,d2['BMI'].mean(), inplace=True)
#columns_to_replace = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
#for column in columns_to_replace:
    #if column in d1.columns:
        #d1[column] = d1[column].replace(0,d1[column][d1[column] != 0].mean())
#j = (df['Glucose']!=0).mean()
#k = (df['BloodPressure']!=0).mean()
#l = (df['SkinThickness']!=0).mean()
#m = (df['Insulin']!=0).mean()
#n = (df['BMI']!=0).mean()
#df['Glucose'] = df['Glucose'].replace(0,j)
#df['BloodPressure'] = df['BloodPressure'].replace(0,k)
#df['SkinThickness'] = df['SkinThickness'].replace(0,l)
#df['Insulin'] = df['Insulin'].replace(0,m)
#df['BMI'] = df['BMI'].replace(0,n)
d1.to_csv("Diabetes_cleaned_data_New.csv")





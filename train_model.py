import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
data = "Diabetes_cleaned_data_New.csv"
df = pd.read_csv(data) 
df = df.drop(df.columns[:2],axis=1)
X = df.drop('Outcome', axis= 1)
y = df['Outcome']

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,'diabetes_app.pkl')
print("The model is saved successfully")
print(df.head())

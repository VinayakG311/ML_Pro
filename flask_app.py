
# A very simple Flask Hello World app for you to get started with...
from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
import sklearn
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
CORS(app,support_credentials=True)

input_data = [
    0,                           # Gender
    -0.37524940647582056,        # Age
    1.697566990208276,           # Sleep Duration
    -0.971686834747765,          # Quality of Sleep
    0.7670134220942246,          # Physical Activity Level
    0.3147253076298664,          # Stress Level
    3,                           # BMI Category
    -1.1185404504731764,         # Heart Rate
    -0.30713741277226986,        # Daily Steps
    -0.45977656779801523,        # Systolic
    -0.7599037156231677,         # Diastolic
    0,                           # Occupation_Accountant
    1,                           # Occupation_Doctor
    0,                           # Occupation_Engineer
    0,                           # Occupation_Lawyer
    0,                           # Occupation_Nurse
    0,                           # Occupation_Salesperson
    0                            # Occupation_Teacher
]

# Convert to a 2D array (1 sample, n features)
gender = {'Female': 0, 'Male': 1}
bmi_category = {'Normal': 0, 'Normal Weight': 1, 'Obese': 2, 'Overweight': 3}
original_occupations = ['Accountant','Doctor','Engineer','Lawyer','Nurse','Salesperson','Teacher']

occupation_columns = ['Occupation_Accountant','Occupation_Doctor','Occupation_Engineer','Occupation_Lawyer','Occupation_Nurse','Occupation_Salesperson','Occupation_Teacher']
def pre_process(X):
  X[['Systolic','Diastolic']] = X['Blood Pressure'].str.split('/',expand=True).apply(pd.to_numeric, errors='coerce')
  # X = pd.get_dummies(X,columns=["Occupation"],prefix="Occupation")
  X.drop('Blood Pressure',axis=1,inplace=True)
  X["Gender"] = X["Gender"].map(gender)
  X["BMI Category"] =  X["BMI Category"].map(bmi_category)
  for col in occupation_columns:
      if col not in X.columns:
          X[col] = False
  occupation = X['Occupation'].iloc[0]
  occupation_column = f'Occupation_{occupation}' if occupation in original_occupations else None
  if occupation_column:
      X[occupation_column] = 1
  X.drop('Occupation',axis=1,inplace=True)
  numerical_features = ["Age","Sleep Duration","Quality of Sleep","Physical Activity Level","Stress Level","Heart Rate","Daily Steps","Diastolic","Systolic"]
  X[numerical_features] = X[numerical_features].apply(pd.to_numeric,errors='coerce')
  with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
  X[numerical_features] = scaler.transform(X[numerical_features])
  return X
  
with open('SVM_Optimised_model.pkl', 'rb') as f:
  model = pickle.load(f)


  
@app.route('/predict', methods=['POST','OPTIONS'])
@cross_origin(supports_credentials=True)
def GetPrediction():
  input_data = request.json
  # print(input_data)
  df = pd.DataFrame([input_data])
  # print(df)
  df = pre_process(df)
  
  with open('SVM_Optimised_model.pkl', 'rb') as f:
    model = pickle.load(f)
  print(df.columns)
  pred = model.predict(df)
  d={}
  d["output"]=pred[0]
  print(pred)
  return jsonify(d)

if __name__ == '__main__':
    app.run(debug=True)
# print(model.predict(input_data))
# app.run(debug=False,host="0.0.0.0",port=4444)
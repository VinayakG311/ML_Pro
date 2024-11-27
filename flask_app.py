
# A very simple Flask Hello World app for you to get started with...
from flask import Flask,request
import sklearn
import pickle
import numpy as np
app = Flask(__name__)

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
input_data = np.array([input_data])
with open('/home/vinayakg311/Random_Forest_Optimised_model.pkl', 'rb') as f:
  model = pickle.load(f)

@app.route('/api/input', methods=['GET'])
def GetPrediction():
  inpt = request.args['query']
  input_data = [float(i) for i in inpt.split(",")]
  input_data = np.array([input_data])
  otpt = model.predict(input_data)
  d={}
  d["output"]=otpt[0]
  print(input)
  return d

# print(model.predict(input_data))
# app.run(debug=False,host="0.0.0.0",port=4444)
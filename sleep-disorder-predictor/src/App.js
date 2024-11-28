import React, { useState } from 'react';
import axios from "axios"; 

function App() {
  const [inputs, setInputs] = useState({});
  const [prediction, setPrediction] = useState(null);

  const handleChange = event => {
    setInputs({ ...inputs, [event.target.name]: event.target.value });
  };

  const handleSubmit = event => {
    event.preventDefault();
    axios.post('http://127.0.0.1:5000/predict',inputs).then(
      res => {
        console.log(res);
        setPrediction(res.data.output)});
    
  };
  const fields = ['Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep', 
          'Physical Activity Level', 'Stress Level', 'BMI Category', 
          'Blood Pressure', 'Heart Rate', 'Daily Steps']
  return (
    <div style={{ width:'350px', margin:'0 auto',padding:'20px', textAlign: 'center' }}>
      <h2>Sleep Disorder Predictor</h2>
      <form onSubmit={handleSubmit}>
        {fields.map((field) => (
          <div key={field} style={{ marginBottom:'10px'}}>
            <label>
              {field}:
              <input 
                type="text" 
                name={field} 
                onChange={handleChange} 
                style={{ width:'100%',padding:'5px',marginTop:'5px' }}
              />
            </label>
          </div>
        ))}
        <button type="submit" style={{ padding:'10px 20px',marginTop:'10px'}}>Predict</button>
      </form>
      {prediction && (
        <div style={{ marginTop:'20px',color: 'red' }}>
          <strong>Prediction:</strong> {prediction}
        </div>
      )}
    </div>
  );
}

export default App;

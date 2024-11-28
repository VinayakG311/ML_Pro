import React, { useState } from 'react';
import { TextField, Button, Typography, Container, Grid } from '@mui/material';

function App() {
  const [inputs, setInputs] = useState({});
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      mode: 'cors',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(inputs),
    });
    const data = await response.json();
    setPrediction(data.output);
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Sleep Disorder Predictor
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={2}>
          {[
            'Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep',
            'Physical Activity Level', 'Stress Level', 'BMI Category', 
            'Blood Pressure', 'Heart Rate', 'Daily Steps'
          ].map((field) => (
            <Grid item xs={12} key={field}>
              <TextField
                name={field}
                label={field}
                variant="outlined"
                fullWidth
                onChange={handleChange}
              />
            </Grid>
          ))}
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Predict
            </Button>
          </Grid>
        </Grid>
      </form>
      {prediction !== null && (
  <Typography variant="h5" align="center" color="secondary" style={{ marginTop: '20px' }}>
    Prediction: {prediction === 'Sleep Apnea' ? 'Sleep Disorder: Sleep Apnea' :
                prediction === 'Insomnia' ? 'Sleep Disorder: Insomnia' :
                prediction === 'None' ? 'No Sleep Disorder' : 'Unknown'}
  </Typography>
)}
    </Container>
  );
}

export default App;

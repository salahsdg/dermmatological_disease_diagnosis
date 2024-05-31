import React from 'react';
import { useLocation } from 'react-router-dom';

const Result = () => {
  const location = useLocation();
  const { predictions, file_url } = location.state;

  return (
    <div>
      <h2>Prediction Results</h2>
      <img src={`http://localhost:8000${file_url}`} alt="Uploaded" style={{ width: '300px' }} />
      <div>
        <p>Class 1: {predictions.class1} ({predictions.prob1}%)</p>
        <p>Class 2: {predictions.class2} ({predictions.prob2}%)</p>
        <p>Class 3: {predictions.class3} ({predictions.prob3}%)</p>
      </div>
    </div>
  );
};

export default Result;

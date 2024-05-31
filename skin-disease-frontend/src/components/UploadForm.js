import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [link, setLink] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleLinkChange = (e) => {
    setLink(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    if (file) {
      formData.append('file', file);
    } else if (link) {
      formData.append('link', link);
    } else {
      setError('Please upload a file or provide a link.');
      return;
    }

    try {
      const response = await axios.post('https://localhost:8000/predictions/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      navigate('/result', { state: { predictions: response.data } });
    } catch (error) {
      setError('An error occurred while uploading.');
    }
  };

  return (
    <div>
      <h2>Upload Image</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="file">File:</label>
          <input type="file" id="file" onChange={handleFileChange} />
        </div>
        <div>
          <label htmlFor="link">Link:</label>
          <input type="text" id="link" value={link} onChange={handleLinkChange} />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default UploadForm;

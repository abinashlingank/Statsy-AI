import React, { useState, useEffect } from "react";
import axios from "axios";
import SERVER_URL from "./config"; // Assuming you've defined the server URL
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [images, setImages] = useState([]);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(`${SERVER_URL}/upload_csv`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setMessage(response.data.message);

      // After uploading, fetch images again to update the list
      fetchImages();
    } catch (error) {
      setMessage("An error occurred while uploading the file.");
      console.error(error);
    }
  };

  const fetchImages = async () => {
    try {
      const response = await axios.get(`${SERVER_URL}/get_images`);
      setImages(response.data.images);
    } catch (error) {
      setMessage("An error occurred while retrieving images.");
      console.error(error);
    }
  };

  return (
    <>
      <center>
        <h1 style={{ color: "chocolate" }}>Statsy AI</h1>
        <p style={{color:"cadetblue"}}>Generate the statistical plots of your data using Llama2 Model</p>
        <p>Just Upload! Get your Statistical Plots!</p>
      </center>
      <div className="App">
        <h1>Upload CSV File</h1>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Upload</button>
        {/* <button onClick={fetchImages}>Get Images</button> Modified to fetch images when clicked */}
        {message && <p>{message}</p>}
        <h2>Statistical Plots for your uploaded data</h2>
        <p style={{ color: "darkcyan" }}>
          The generated plots using Llama2 model will be shown here
        </p>
        <div className="image-container">
          {images.map((image, index) => (
            <img
              key={index}
              src={`${SERVER_URL}/output/${image}`}
              alt={`Image ${index}`}
            />
          ))}
        </div>
      </div>
    </>
  );
}

export default App;

import React, { useState } from "react";
import axios from "axios";
 
function App() {
 
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
 
  const sendFile = async () => {
 
    const formData = new FormData();
    formData.append("file", file);
 
    const response = await axios.post(
      "http://localhost:8000/summarize",
      formData
    );
 
    setSummary(response.data.summary);
  };
 
  return (
<div style={{ padding: 40 }}>
<h2>PDF Summarizer</h2>
 
      <input
        type="file"
        onChange={(e)=>setFile(e.target.files[0])}
      />
 
      <button onClick={sendFile}>
        Enviar
</button>
 
      <h3>Resumo</h3>
 
      <p>{summary}</p>
</div>
  );
}
 
export default App;
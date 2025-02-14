import React, { useState } from "react";
import axios from "axios";

function App() {
    const [query, setQuery] = useState("");
    const [response, setResponse] = useState("");

    const handleSearch = async () => {
        const res = await axios.get(`http://localhost:8000/search?query=${query}`);
        setResponse(res.data.generated_response);
    };

    return (
        <div>
            <h1>RAG Chatbot</h1>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter research query..."
            />
            <button onClick={handleSearch}>Search</button>
            <h3>Response:</h3>
            <p>{response}</p>
        </div>
    );
}

export default App;


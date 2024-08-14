// index.js
const express = require('express');
const axios = require('axios');
const cors = require('cors');  // Import the cors package

const app = express();
app.use(express.json());
app.use(cors());  // Enable CORS for all routes

app.post('/generate', async (req, res) => {
    console.log('req',req.body)
    try {
        const response = await axios.post('http://localhost:5001/generate', req.body);
        console.log('response', response)
        res.json(response.data);
    } catch (error) {
        console.log(error,'error in api gateway')
        res.status(500).send(error.message);
    }
});

app.listen(3000, () => {
    console.log('API Gateway running on port 3000');
});

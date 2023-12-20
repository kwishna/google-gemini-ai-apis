const axios = require('axios');
require('dotenv').config()

let data = JSON.stringify({
  "model": "models/embedding-001",
  "content": {
    "parts": [
      {
        "text": "Write the definition of embedding."
      }
    ]
  }
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent?key=' + process.env.GOOGLE_API_KEY,
  headers: {
    'Content-Type': 'application/json'
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});

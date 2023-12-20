const axios = require('axios');
require('dotenv').config()

let data = JSON.stringify({
  "contents": [
    {
      "parts": [
        {
          "text": "Write long a story about a magic backpack."
        }
      ]
    }
  ]
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:streamGenerateContent?key=' + process.env.GOOGLE_API_KEY,
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

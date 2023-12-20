const axios = require('axios');
require('dotenv').config()

let data = JSON.stringify({
  "contents": [
    {
      "parts": [
        {
          "text": "What is this picture?"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII="
          }
        }
      ]
    }
  ]
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key=' + process.env.GOOGLE_API_KEY,
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

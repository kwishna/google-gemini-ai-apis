const axios = require('axios');
require('dotenv').config()

let config = {
  method: 'get',
  maxBodyLength: Infinity,
  url: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro?key=' + process.env.GOOGLE_API_KEY,
  headers: { }
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});

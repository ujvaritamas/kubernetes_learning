const express = require('express');
const os = require('os');

const app = express();

app.get('/', (req, res) => {
  console.log("get request"+ req);
  res.send('Successful response.' + os.hostname);
});

app.listen(3000, () => console.log('Example app is listening on port 3000.'));
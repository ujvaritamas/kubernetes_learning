import express from 'express';
import fetch from 'node-fetch';
import os from 'os';

const app = express();
const PORT = 3000

app.get('/', (req, res) => {
  console.log("VERSION2 get request"+ req);
  res.send('Successful response.' + os.hostname);
});

app.get('/nginx', async (req, res) => {
  const url='http://nginx';
  const response = await fetch(url);
  const body = await response.text();
  res.send(body);
});


app.listen(PORT, () => console.log('Example app is listening on port' + PORT +'.'));
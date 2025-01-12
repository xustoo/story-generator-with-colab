const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const storyRoutes = require('./routes/storyRoutes');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());
app.use('/api/stories', storyRoutes);

app.listen(PORT, () => {
  console.log(`Backend server is running at http://192.168.20.68:${PORT}`);
});

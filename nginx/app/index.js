const express = require("express");
const app = express();
const PORT = 3000;
const VERSION = "v1.0";

app.get('/', (req, res) => {
    res.send(`Running version ${VERSION}`);
});

app.listen(PORT, () => {
    console.log(`App running on port ${PORT}`)
})

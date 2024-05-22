const express = require("express");
const cors = require("cors");
const app = express();
const port = 3000;

app.use(cors());

app.use(express.json());

app.get("/api/data", (req, res) => {
  res.json({ message: "This is a CORS-enabled response" });
});

app.post("/api/simple", (req, res) => {
  res.json({ message: "Simple request received", data: req.body });
});

app.post("/api/preflight", (req, res) => {
  res.json({ message: "Preflight request received", data: req.body });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

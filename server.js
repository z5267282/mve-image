const express = require("express");
const app = express();

const PORT = 4400;

// Serve static files from the current directory
app.use(express.static(__dirname));

let connection = null;

app.get("/message", (req, res) => {
  const { v } = req.query;

  if (connection === null) {
    res.sendStatus(401);
  } else {
    connection.write(`data: ${v}\n\n`);
    res.sendStatus(200);
  }
});

// Handle the /play route
app.get("/listen", (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Connection", "keep-alive");
  res.flushHeaders();

  connection = res;

  req.on("close", () => (connection = null));
});

// Start the server
app.listen(PORT, () => {
  console.log(`server is running on http://localhost:${PORT}`);
});

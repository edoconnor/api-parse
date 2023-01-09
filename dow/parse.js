const fs = require("fs");

fs.readFile("data.csv", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});

const rows = data.split("\n");

const aaplRows = rows.filter((row) => {
  const cells = row.split(",");
  return cells[1] === "AAPL";
});

const lastFive = aaplRows.slice(-5);

lastFive.forEach((row) => {
  const cells = row.split(",");
  const date = cells[2];
  const close = cells[3];
  console.log(date, close);
});

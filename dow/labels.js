const csv = "dow30_last5_close.csv";

const lines = csv.split('\n');

const axpLines = lines.filter(line => line.includes('AXP'));

const axpData = axpLines.map(line => {
  const [symbol, date, close] = line.split(',');
  return { date, close };
});

let axp_date;
let axp_close;

axpData.forEach(data => {
  axp_date = data.date;
  axp_close = data.close;
});

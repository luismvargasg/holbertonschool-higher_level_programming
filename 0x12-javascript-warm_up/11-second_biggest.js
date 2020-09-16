#!/usr/bin/node
if (parseInt(process.argv[3])) {
  const res = process.argv;
  const newRes = res.slice(2);
  newRes.sort((a, b) => a - b);
  console.log(newRes[newRes.length - 2]);
} else {
  console.log('0');
}

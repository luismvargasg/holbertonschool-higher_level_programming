#!/usr/bin/node
if (parseInt(process.argv[3])) {
  const res = process.argv.sort();
  console.log(res[res.length - 2]);
} else {
  console.log('0');
}

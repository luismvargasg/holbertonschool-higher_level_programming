#!/usr/bin/node
function factorial (n) {
  let resFact;
  if (!n || n === 0) {
    resFact = 1;
  } else {
    resFact = n * factorial(n - 1);
  }
  return resFact;
}

const res = factorial(parseInt(process.argv[2]));
console.log(res);

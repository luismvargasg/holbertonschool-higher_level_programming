#!/usr/bin/node
const myArray = ['C is fun'];
if (process.argv[2]) {
  for (let step = 0; step < process.argv[2]; step++) {
    console.log(myArray[0]);
  }
} else {
  console.log('Missing number of occurrences');
}

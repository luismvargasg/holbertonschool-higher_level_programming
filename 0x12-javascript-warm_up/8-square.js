#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let step = 0; step < process.argv[2]; step++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}

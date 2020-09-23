#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const myDict = {};
    JSON.parse(body).forEach(function (data) {
      if (data.completed) {
        const id = data.userId;
        if (!(id in myDict)) {
          myDict[id] = 0;
        }
        myDict[id] += 1;
      }
    });
    console.log(myDict);
  }
});

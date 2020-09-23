#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const str = '18';
let res = 0;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const movie of JSON.parse(body).results) {
      for (const character of movie.characters) {
        if (character.includes(str)) {
          res++;
        }
      }
    }
    console.log(res);
  }
});

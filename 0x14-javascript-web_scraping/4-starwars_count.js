#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const str = '18';
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let res = 0;
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

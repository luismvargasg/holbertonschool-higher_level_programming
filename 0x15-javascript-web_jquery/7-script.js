const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, {
  tags: 'name'
}, function (json) {
  $('DIV#character').text(json.name);
});

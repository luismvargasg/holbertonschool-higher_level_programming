const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (data) {
  $.each(data.results, function (i, item) {
    $('UL#list_movies').append('<li>' + item.title + '</li>');
  });
});

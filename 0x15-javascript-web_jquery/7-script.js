$(document).ready(function () {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(apiUrl, function (data) {
    $.each(data.results, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});

$.getJSON('http://swapi.co/api/films?format=json',
  function (res) {
    $.each(res.results, function (k, v) {
      $('UL#list_movies').append($('<li></li>').text(v.title));
    });
  }
);

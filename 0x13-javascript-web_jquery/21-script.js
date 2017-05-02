$.ajax({
  url: 'http://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (res) {
    $('DIV#character').text(res.name);
  }
});
